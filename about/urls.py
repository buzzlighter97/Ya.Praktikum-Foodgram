from django.urls import path

from about import views

urlpatterns = [
    path('author/', views.AboutView.as_view(), name='author'),
    path('spec/', views.SpecView.as_view(), name='spec'),
]
