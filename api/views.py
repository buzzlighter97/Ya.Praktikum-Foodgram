from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import (FavoriteSerializer, FollowSerializer,
                             IngredientSerializer, ShoppingListSerializer)
from recipes.models import Favorite, Follow, Ingredient, ShoppingList


@api_view(['GET'])
def ingredients(request):
    query = request.GET.get('query')
    ingredient = Ingredient.objects.filter(title__istartswith=query)
    serializer = IngredientSerializer(ingredient, many=True)
    return Response(serializer.data)


@api_view(['POST', 'DELETE'])
def purchases(request, id=None):
    if request.method == 'POST':
        data = {
            'recipe': request.data['id'],
            'user': request.user.id
        }
        serializer = ShoppingListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({'fail': False}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        item = ShoppingList.objects.get(recipe__id=id)
        if item.delete():
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'fail': False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'DELETE'])
def favorites(request, id=None):
    user = request.user
    if request.method == 'POST':
        data = {
            'recipe': request.data['id'],
            'user': user.id
        }
        serializer = FavoriteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'fail': False}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        item = Favorite.objects.get(user=user, recipe__id=id)
        if item.delete():
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'fail': False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'DELETE'])
def subscriptions(request, id=None):
    user = request.user
    if request.method == 'POST':
        data = {
            'author': request.data['id'],
            'user': user.id
        }
        serializer = FollowSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'fail': False}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        item = Follow.objects.get(user=user, author__id=id)
        if item.delete():
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'fail': False}, status=status.HTTP_400_BAD_REQUEST)
