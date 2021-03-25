from recipes.models import ShoppingList


def get_shopping_list_elements_length(request):

    if not request.user.is_anonymous:
        user = request.user
        shopping_list_length = (ShoppingList.objects
                                .filter(user=user)
                                .count())

        return {
            'shopping_list_length': shopping_list_length
        }
    return {}
