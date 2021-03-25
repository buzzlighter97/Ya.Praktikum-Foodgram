import random
import string

from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.text import slugify

from users.models import User


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Автор'
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    image = models.ImageField(
        upload_to='recipe',
        verbose_name='Картинка'
    )
    description = models.TextField(
        max_length=300,
        verbose_name='Описание'
    )
    tag = ArrayField(
        base_field=models.CharField(max_length=10,),
        verbose_name='Теги'
    )
    time = models.IntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(1)]
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    slug = models.SlugField(
        max_length=200,
        verbose_name='Слаг'
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        letters = string.ascii_lowercase

        while Recipe.objects.filter(slug=self.slug).exists():
            self.slug += random.choice(letters)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-date_created',)


class Ingredient(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    dimension = models.CharField(
        max_length=10,
        verbose_name='Единица измерения'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredient',
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe_ingredient',
        verbose_name='Ингредиент'
    )
    amount = models.IntegerField(
        verbose_name='Количество',
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f'{self.recipe} - {self.ingredient} - {self.amount}'

    class Meta:
        verbose_name = 'Количество'
        verbose_name_plural = 'Количество'


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Рецепт'
    )

    class Meta:
        UniqueConstraint(
            name='unique_user_shoppinglist',
            fields=['user', 'recipe'],
        )
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        UniqueConstraint(
            name='unique_follow',
            fields=['user', 'author'],
        )
        verbose_name = 'Подписчики'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return f'{self.user} подписался на {self.author}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favourite',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favourite',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
