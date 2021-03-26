from django.urls import include, path

from api import views

urlpatterns = [
    path(
        'v1/',
        include(
            [
                path(
                    'ingredients/',
                    views.IngredientAPIView.as_view(),
                    name='ingredients'
                ),
                path(
                    'favorites/',
                    views.FavoriteCreateView.as_view(),
                    name='favorite_create'
                ),
                path(
                    'favorites/<int:id>/',
                    views.FavoriteDeleteView.as_view(),
                    name='favorite_delete'
                ),
                path(
                    'purchases/',
                    views.PurchaseCreateView.as_view(),
                    name='purchase_create'
                ),
                path(
                    'purchases/<int:id>/',
                    views.PurchaseDeleteView.as_view(),
                    name='purchase_delete'
                ),
                path(
                    'subscriptions/',
                    views.SubscribeCreateView.as_view(),
                    name='subscribe_create'
                ),
                path(
                    'subscriptions/<int:id>/',
                    views.SubscribeDeleteView.as_view(),
                    name='subscribe_delete'
                )
            ]
        )
    )
]
