from django.db import models
from users.models import User

class Ingredients(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='название')
    units = models.CharField(max_length=10, null=False, blank=False, verbose_name='единицы измерения')

class IngredientsToAdd(models.Model):
    ingredient = models.ForeignKey(Ingredients, null=False, blank=False, on_delete=models.PROTECT, related_name='+', verbose_name='пара ингредиент/ед.изм.')
    quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name='количество')

class Recipes(models.Model):
    TAGS = [
        ('BR', 'Завтрак'),
        ('LA', 'Обед'),
        ('DI', 'Ужин'),
    ]
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='recipes', verbose_name='автор')
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='название')
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(null=False, blank=False, verbose_name='описание')
    ingredients = models.ForeignKey(IngredientsToAdd, null=False, blank=False, on_delete=models.DO_NOTHING, verbose_name='ингредиенты')
    tag = models.CharField(max_length=10, choices=TAGS, null=False, blank=False, verbose_name='теги')
    time = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='время приготовления')
    slug = models.SlugField(null=False, blank=False, verbose_name='уникальная часть URL')
    pub_date = models.DateTimeField(null=False, blank=False, verbose_name='дата и время публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
