from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'author_recipes/<str:slug>/',
        views.author_recipes,
        name='author_recipes'
    ),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('favorites/', views.favorites, name='favorites'),
    path(
        'single_recipe/<str:slug>/',
        views.single_recipe,
        name='single_recipe'
    ),
    path('edit_recipe/<str:slug>/', views.edit_recipe, name='edit_recipe'),
    path('followers/', views.followers, name='followers'),
    path(
        'remove_recipe/<str:slug>/',
        views.remove_recipe,
        name='remove_recipe'
    ),
    path(
        'download_shopping_list/',
        views.download_shopping_list,
        name='download_shopping_list'
    ),
]
