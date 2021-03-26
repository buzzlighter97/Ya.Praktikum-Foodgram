from decimal import Decimal

from recipes.models import Recipe


def filter_tag(request):
    tags = request.GET.get('tags', 'bld')
    recipe_list = Recipe.objects.filter(tags__slug__in=tags).distinct()
    return recipe_list, tags


def get_dict_ingredients(request):
    ingredients = {}
    for key, ingredient_name in request.POST.items():
        if 'nameIngredient' in key:
            _ = key.split('_')
            ingredients[ingredient_name] = Decimal(
                request.POST[f'valueIngredient_{_[1]}'].replace(',', '.')
            )
    return ingredients
