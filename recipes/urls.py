from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path(
        'recipes/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'
    ),
    path(
        'recipes/<int:recipe_id>/delete/',
        views.recipe_delete,
        name='recipe_delete',
    ),
    path('recipes/new/', views.create_recipe, name='create_recipe'),
    path('recipes/<str:username>/', views.profile, name='profile'),
    path('recipes/', views.index, name='recipes'),
    path('favorites/', views.favorites, name='favorites'),
    path('purchases/', views.shopping_list, name='purchases'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('shoplist/', views.get_ingredients, name='shoplist'),
]
