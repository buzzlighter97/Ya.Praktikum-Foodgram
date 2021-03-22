from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
#    path('<str:username>/', name='author'),
#    path('<str:username>/recipes/', name='recipes'),
#    path('<str:username>/recipes/<int:id>/', name='recipe')
#    path('purchases/', views.all_purchases_view()),
#    path('purchases/<int:id>/', views.purchase_detail_view()),
#    path('subscriptions/', views.all_subscriptions_view()),
#    path('subscriptsions/<int:id>/', views.remove_subscription_view()),
#    path('favorites/', views.add_favorites_view()),
#    path('favorites/<int:id>/', views.remove_favorite_view()),
#    path('ingredients?query=${text}', views.get_ingredients_view())
]
