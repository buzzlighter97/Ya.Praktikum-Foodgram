from django import template

from api.models import Favorite, Purchase, Subscribe

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def in_favorites(value, user):
    return Favorite.objects.filter(recipe=value, user=user).exists()


@register.filter
def in_shopping_list(value, user):
    return Purchase.objects.filter(recipe=value, user=user).exists()


@register.filter
def in_subscription(value, user):
    return Subscribe.objects.filter(author=value, user=user).exists()
