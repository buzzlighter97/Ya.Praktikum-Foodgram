from django.shortcuts import get_object_or_404
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Favorite, Purchase, Subscribe
from api.serializers import (FavoriteSerializer, IngredientSerializer,
                             PurchaseSerializer, SubscribeSerializer)
from recipes.models import Ingredient, Recipe
from users.models import User


class CreateResponseView:
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"success": True})
        return Response({"success": False})


class IngredientAPIView(generics.ListAPIView):
    """Класс для поиска в базе ингредиентов по их названиям."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', ]


class FavoriteCreateView(CreateResponseView, generics.CreateAPIView):
    """Класс для добавления рецепта в избранное."""
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class FavoriteDeleteView(APIView):
    """Класс для удаления рецепта из избранного."""
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        favorite = recipe.in_favorite.filter(user=request.user)
        return Response({"success": bool(favorite.delete())})


class PurchaseCreateView(CreateResponseView, generics.CreateAPIView):
    """Класс для добавления рецепта в список покупок."""
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseDeleteView(APIView):
    """Класс для удаления рецепта из списка покупок."""
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        purchase = recipe.in_purchases.filter(user=request.user)
        return Response({"success": bool(purchase.delete())})


class SubscribeCreateView(CreateResponseView, generics.CreateAPIView):
    """Класс для добавления автора в подписку."""
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class SubscribeDeleteView(APIView):
    """Класс для удаления автора из подписки."""
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        author = get_object_or_404(User, id=id)
        subscribe = author.following.filter(user=request.user)
        return Response({"success": bool(subscribe.delete())})
