from rest_framework import serializers

from recipes.models import Favorite, Follow, Ingredient, Recipe, ShoppingList
from users.models import User


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ingredient


class ShoppingListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:
        fields = '__all__'
        model = ShoppingList


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:
        fields = '__all__'
        model = Favorite


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow
