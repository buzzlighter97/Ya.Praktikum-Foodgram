from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from foodgram.settings import RECIPES_ON_PAGE
from users.models import User

from recipes.forms import RecipeForm
from recipes.models import Recipe, Ingredient, IngredientAmount, Tag
from recipes.utils import filter_tag, get_dict_ingredients


def index(request):
    recipe_list, tags = filter_tag(request)
    paginator = Paginator(recipe_list, RECIPES_ON_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'indexAuth.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
        },
    )


@login_required
def create_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    user = get_object_or_404(User, username=request.user)
    ingredients = get_dict_ingredients(request)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = user
        recipe.save()

        tags = form.cleaned_data['tag']
        for tag in tags:
            recipe_tag = Tag(recipe=recipe, title=tag)
            recipe_tag.save()

        for key, value in ingredients.items():
            ingredient = get_object_or_404(Ingredient, title=key)
            recipe_ing = IngredientAmount(
                recipe=recipe, ingredient=ingredient, amount=value
            )
            recipe_ing.save()
        form.save_m2m()
        return redirect('recipes')
    return render(request, 'formRecipe.html', {'form': form})


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'singlePage.html', {'recipe': recipe})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    recipe_list, tags = filter_tag(request)
    recipe_list = recipe_list.filter(author=author)
    paginator = Paginator(recipe_list, RECIPES_ON_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'authorRecipe.html',
        {
            'page': page,
            'paginator': paginator,
            'username': username,
            'tags': tags,
        },
    )


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author:
        return redirect('recipe_view', recipe_id=recipe_id)
    form = RecipeForm(
        request.POST or None, files=request.FILES or None, instance=recipe
    )
    ingredients = get_dict_ingredients(request)

    if form.is_valid():
        IngredientAmount.objects.filter(recipe=recipe).delete()
        Tag.objects.filter(recipe=recipe).delete()
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()

        tags = form.cleaned_data['tag']
        for tag in tags:
            recipe_tag = Tag(recipe=recipe, title=tag)
            recipe_tag.save()

        for key, value in ingredients.items():
            ingredient = get_object_or_404(Ingredient, title=key)
            recipe_ing = IngredientAmount(
                recipe=recipe, ingredient=ingredient, amount=value
            )
            recipe_ing.save()
        form.save_m2m()
        return redirect('recipe_view', recipe_id=recipe_id)
    tags = list(recipe.tags.values_list('title', flat=True))
    return render(
        request,
        'formChangeRecipe.html',
        {'form': form, 'recipe': recipe, 'tags': tags},
    )


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
        return redirect('profile', username=request.user.username)
    return redirect('recipes')


@login_required
def favorites(request):
    recipe_list, tags = filter_tag(request)
    recipe_list = recipe_list.filter(in_favorite__user=request.user)
    paginator = Paginator(recipe_list, RECIPES_ON_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'favorite.html',
        {'page': page, 'paginator': paginator, 'tags': tags},
    )


@login_required
def shopping_list(request):
    recipe_list, tags = filter_tag(request)
    recipe_list = recipe_list.filter(in_purchases__user=request.user)
    return render(
        request, 'shopList.html', {'recipe_list': recipe_list, 'tags': tags}
    )


@login_required
def subscriptions(request):
    authors = User.objects.filter(following__user=request.user)
    paginator = Paginator(authors, RECIPES_ON_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, 'myFollow.html', {'page': page, 'paginator': paginator}
    )


def get_ingredients(request):
    text = ''
    list = (
        Recipe.objects.filter(in_purchases__user=request.user)
        .order_by("ingredients__title")
        .values("ingredients__title", "ingredients__dimension")
        .annotate(amount=Sum("quantity__amount"))
    )

    for ingredient in list:
        text += (
            f"{ingredient['ingredients__title']} "
            f"({ingredient['ingredients__dimension']})"
            f" \u2014 {ingredient['amount']} \n"
        )

    filename = "ingredients.txt"
    response = HttpResponse(text, content_type="text/plain")
    response["Content-Disposition"] = f"attachment; filename={filename}"
    return response
