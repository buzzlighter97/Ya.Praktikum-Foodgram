from django.http.response import HttpResponseForbidden
from . import models
from django.shortcuts import redirect, render
from . import forms

def index_view(request):
    recipes = models.Recipes.objects.all()
    context = {'recipes': recipes}
    return render(request, 'templates/indexAuth.html', context)

def add_recipe(request):
    if request.method == 'GET':
        form = forms.RecipeForm()
        context = {
            'form': form
        }
        return render(request, 'templates/formRecipe.html', context)
    elif request.method == 'POST':
        form = forms.RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            recipe_id = models.Recipes.objects.all(author__username=user.username).latest
            return redirect('recipe', username=user.username, id=recipe_id)
    else:
        return HttpResponseForbidden(request)