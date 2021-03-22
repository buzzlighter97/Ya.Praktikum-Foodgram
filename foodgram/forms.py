from django import forms
from .models import IngredientsToAdd, Recipes

class RecipeForm(forms.ModelForm):
    TAGS = [
        ('BR', 'Завтрак'),
        ('LA', 'Обед'),
        ('DI', 'Ужин'),
    ]
    title = forms.CharField(max_length=50, label='Название блюда', initial='Колбаски по-пражски')
    image = forms.ImageField(label='Изображение готового блюда')
    description = forms.CharField(initial='Вкусно опишите готовое блюдо', label='Описание')
    ingredients = forms.ModelMultipleChoiceField(queryset=IngredientsToAdd.objects.all(), label='Ингредиенты')
    quantity = forms.IntegerField(min_value=0, label='Количество')
    tags = forms.MultipleChoiceField(choices=TAGS, label='Теги')
    time = forms.IntegerField(min_value=0, max_value=300 , label='Время приготовления в минутах')

    class Meta:
        model = Recipes
        fields = ('title', 'image', 'description', 'ingredients', 'quantity', 'tags', 'time')