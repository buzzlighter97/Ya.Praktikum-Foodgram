from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from foodgram_project.settings import COUNT_RECIPE
from recipes.forms import RecipeForm
from recipes.models import (Favorite, Follow, Recipe, RecipeIngredient,
                            ShoppingList)
from recipes.utils import tags_filter
from users.models import User


def index(request):
    shopping_list_ids = None
    favorites_ids = None
    recipes, tag = tags_filter(request)

    paginator = Paginator(recipes, COUNT_RECIPE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if not request.user.is_anonymous:
        user = request.user
        shopping_list_ids = (ShoppingList.objects
                             .filter(user=user)
                             .values_list('recipe', flat=True))
        favorites_ids = (Favorite.objects
                         .filter(user=user)
                         .values_list('recipe', flat=True))

    context = {
        'tag': tag,
        'shopping_list_ids': shopping_list_ids,
        'favorites_ids': favorites_ids,
        'page': page,
        'paginator': paginator
    }

    return render(request, 'index.html', context)


def author_recipes(request, slug):
    shopping_list_ids = None
    favorites_ids = None
    followers_ids = None
    recipes, tag = tags_filter(request, author=slug)
    author_id = get_object_or_404(User, username=slug).id

    paginator = Paginator(recipes, COUNT_RECIPE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if not request.user.is_anonymous:
        user = request.user
        shopping_list_ids = (ShoppingList.objects
                             .filter(user=user)
                             .values_list('recipe', flat=True))
        favorites_ids = (Favorite.objects
                         .filter(user=user)
                         .values_list('recipe', flat=True))
        followers_ids = (Follow.objects
                         .filter(user=user)
                         .values_list('author', flat=True))

    context = {
        'tag': tag,
        'shopping_list_ids': shopping_list_ids,
        'favorites_ids': favorites_ids,
        'author': slug,
        'author_id': author_id,
        'followers_ids': followers_ids,
        'page': page,
        'paginator': paginator
    }

    return render(request, 'author_recipes.html', context)


def single_recipe(request, slug):
    favorites_ids = None
    shopping_list_ids = None
    followers_ids = None
    recipe = get_object_or_404(Recipe, slug=slug)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    if not request.user.is_anonymous:
        user = request.user
        favorites_ids = (Favorite.objects
                         .filter(user=user)
                         .values_list('recipe', flat=True))
        shopping_list_ids = (ShoppingList.objects
                             .filter(user=user)
                             .values_list('recipe', flat=True))
        followers_ids = (Follow.objects
                         .filter(user=user)
                         .values_list('author', flat=True))

    context = {
        'recipe': recipe,
        'favorites_ids': favorites_ids,
        'shopping_list_ids': shopping_list_ids,
        'followers_ids': followers_ids,
        'ingredients': ingredients,
    }
    return render(request, 'single_recipe.html', context)


@login_required
def create_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(
            request.POST,
            request.FILES,
            username=request.user
        )
        if recipe_form.is_valid():
            recipe_form.save()

        return redirect('index')
    else:
        form = RecipeForm(username=request.user)

    user = request.user
    shopping_list_ids = (ShoppingList.objects
                         .filter(user=user)
                         .values_list('recipe', flat=True))
    context = {
        'form': form,
        'shopping_list_ids': shopping_list_ids,
    }
    return render(request, 'create_recipe.html', context=context)


@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    my_shopping_list = ShoppingList.objects.filter(user=request.user)

    if request.method == 'POST':
        RecipeIngredient.objects.filter(recipe=recipe).delete()

        recipe_form = RecipeForm(
            request.POST,
            request.FILES,
            username=request.user,
            instance=recipe,
        )

        if recipe_form.is_valid():
            recipe_form.save()

        return redirect('index')
    else:
        form = RecipeForm(username=request.user, instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
        'ingredients': ingredients,
        'shopping_list_ids': my_shopping_list,
    }
    return render(request, 'edit_recipe.html', context)


@login_required
def favorites(request):
    user = request.user
    favourites = Favorite.objects.filter(user=user)
    if not favourites:
        favourites = [-1]

    recipes, tag = tags_filter(request, favourites=favourites)
    paginator = Paginator(recipes, COUNT_RECIPE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    shopping_list_ids = (ShoppingList.objects
                         .filter(user=user)
                         .values_list('recipe', flat=True))
    favorites_ids = (Favorite.objects
                     .filter(user=user)
                     .values_list('recipe', flat=True))

    context = {
        'tag': tag,
        'shopping_list_ids': shopping_list_ids,
        'favorites_ids': favorites_ids,
        'page': page,
        'paginator': paginator
    }
    return render(request, 'favorite.html', context)


@login_required
def followers(request):
    user = request.user

    my_followers = Follow.objects.filter(user=user)
    recipes = Recipe.objects.filter(author__following__in=my_followers)
    shopping_list_ids = (ShoppingList.objects
                         .filter(user=user)
                         .values_list('recipe', flat=True))
    context = {
        'my_followers': my_followers,
        'recipes': recipes,
        'shopping_list_ids': shopping_list_ids,
    }
    return render(request, 'followers.html', context)


def shopping_list(request):
    user = request.user
    my_shopping_list = ShoppingList.objects.filter(user=user)
    recipes = Recipe.objects.filter(shopping_list__in=my_shopping_list)

    context = {
        'shopping_list_ids': my_shopping_list,
        'recipes': recipes,
    }
    return render(request, 'shopping_list.html', context=context)


def remove_recipe(request, slug):
    Recipe.objects.filter(slug=slug).delete()
    return redirect('index')


def download_shopping_list(request):
    ingredients = (RecipeIngredient.objects
                   .filter(recipe__shopping_list__user=request.user)
                   .select_related('ingredient'))
    items = {}
    for item in ingredients:
        title = item.ingredient.title
        dimension = item.ingredient.dimension
        amount = item.amount
        if not items.get(title):
            items[title] = [amount, dimension]
        else:
            items[title] = [items[title][0] + amount, dimension]
    if items:
        file_data = [f'{k.capitalize()}: {v[0]} {v[1]}\n'
                     for k, v in items.items()]
        response = HttpResponse(
            file_data,
            content_type='application/text charset=utf-8'
        )
        response['Content-Disposition'] = ('attachment; '
                                           'filename="shopping_list.txt"')
        return response
    return redirect('index')


def page_not_found(request, exception):
    return render(
        request,
        'errors/404.html',
        {'path': request.path},
        status=404
    )


def server_error(request):
    return render(request, 'errors/500.html', status=500)
