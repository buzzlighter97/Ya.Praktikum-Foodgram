from django.urls import path

from api import views

urlpatterns = [
    path('purchases/', views.purchases, name='create_purchase'),
    path('purchases/<int:id>/', views.purchases, name='delete_purchase'),
    path('subscriptions/', views.subscriptions, name='create_subscription'),
    path(
        'subscriptions/<int:id>/',
        views.subscriptions,
        name='delete_subscription'
    ),
    path('favorites/', views.favorites, name='create_favorite'),
    path('favorites/<int:id>/', views.favorites, name='delete_favorite'),
    path('ingredients/', views.ingredients, name='list_ingredients'),
]
