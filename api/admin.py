from django.contrib import admin

from api.models import Favorite, Purchase, Subscribe


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')


admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Purchase, PurchaseAdmin)
