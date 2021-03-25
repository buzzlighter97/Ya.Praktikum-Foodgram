from django.contrib import admin
from django.db.models import Count

from recipes.models import (Favorite, Follow, Ingredient, Recipe,
                            RecipeIngredient, ShoppingList)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    def favorite_count(self, obj):
        return obj.favorite_count

    favorite_count.short_description = "Счетчик избранного"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(favorite_count=Count("favourite"))
        return queryset

    list_display = ('name', 'author', 'favorite_count')
    search_fields = ('name', 'author__username', 'tag')
    inlines = [
        RecipeIngredientInline,
    ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'dimension')
    search_fields = ('title',)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_filter = ('amount',)


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_filter = ('user',)
