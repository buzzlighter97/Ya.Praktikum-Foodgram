from django.contrib import admin
from django.db.models import Count

from recipes.models import Ingredient, IngredientAmount, Recipe, Tag


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    min_num = 1
    extra = 0
    verbose_name = 'Ингредиент'


class TagInline(admin.TabularInline):
    model = Tag
    min_num = 1
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAmountInline, TagInline)
    list_display = (
        'id', 'title', 'author', 'get_favorite',
        'image_img', 'duration', 'get_tag',
    )
    list_filter = ('author', 'tags__title', )
    search_fields = ('title', 'author__username', )
    autocomplete_fields = ('author', )
    ordering = ('-pub_date', )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(_get_favorite=Count('in_favorite'))

    def get_tag(self, obj):
        return list(obj.tags.values_list('title', flat=True))

    def get_favorite(self, obj):
        return obj._get_favorite

    get_tag.short_description = 'Теги'
    get_favorite.short_description = 'Добавлен в избранное, раз'
    get_favorite.admin_order_field = '_get_favorite'


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'dimension', )
    search_fields = ('^title', )


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'recipe', )


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientAmount, RecipeIngredientAdmin)
admin.site.register(Tag, TagAdmin)
