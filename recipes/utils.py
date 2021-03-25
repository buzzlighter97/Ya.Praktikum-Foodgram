from recipes.models import Recipe


def tags_filter(request, author=None, favourites=None):
    state = ['breakfast', 'lunch', 'dinner']
    breakfast = request.GET.get('breakfast')
    lunch = request.GET.get('lunch')
    dinner = request.GET.get('dinner')
    if breakfast:
        state[0] = None
    if lunch:
        state[1] = None
    if dinner:
        state[2] = None

    if author:
        recipes = (Recipe.objects
                   .select_related('author')
                   .prefetch_related('recipe_ingredient')
                   .filter(tag__overlap=state, author__username=author))
    elif favourites:
        recipes = (Recipe.objects
                   .select_related('author')
                   .prefetch_related('recipe_ingredient')
                   .filter(tag__overlap=state, favourite__in=favourites))
    else:
        recipes = (Recipe.objects
                   .select_related('author')
                   .prefetch_related('recipe_ingredient')
                   .filter(tag__overlap=state))

    tag = {key: 'tags__checkbox_active' for key in state}

    return recipes, tag
