from django.core.exceptions import ValidationError
from django.db import models

from recipes.models import Recipe
from users.models import User


class Favorite(models.Model):
    """ORM-модель 'Избранное'."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='in_favorite',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_favorites'
            )
        ]

    def __str__(self):
        return f'{self.user.username} добавил в избранное {self.recipe.title}'

    def clean(self):
        if self.user == self.recipe.author:
            raise ValidationError(
                'Нельзя добавлять в избранное собственные рецепты'
            )


class Subscribe(models.Model):
    """ORM-модель 'Подписка'."""
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
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'], name='unique_subscriptions'
            )
        ]

    def __str__(self):
        return f'{self.user.username} подписался на {self.author.username}'

    def clean(self):
        if self.author == self.user:
            raise ValidationError('Нельзя подписываться на самого себя')


class Purchase(models.Model):
    """ORM-модель 'Покупка'."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='in_purchases',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_purchases'
            )
        ]

    def __str__(self):
        return f'{self.user.username} добавил в покупки {self.recipe.title}'
