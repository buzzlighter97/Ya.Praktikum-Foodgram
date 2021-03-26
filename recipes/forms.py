from django import forms

from recipes.models import Recipe, Tag


class RecipeForm(forms.ModelForm):
    """Класс форма для создания новых рецептов."""
    TAG_CHOICES = (
        (Tag.TITLE_BREAKFAST_RU, Tag.COLOR_ORANGE),
        (Tag.TITLE_LUNCH_RU, Tag.COLOR_GREEN),
        (Tag.TITLE_DINNER_RU, Tag.COLOR_PURPLE),
    )

    tag = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=TAG_CHOICES,
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form__textarea'})
    )

    class Meta:
        model = Recipe
        fields = ('title', 'tag', 'duration', 'text', 'image')
