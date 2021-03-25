from django import forms

from recipes.models import Ingredient, Recipe, RecipeIngredient

TAGS = [
    ('breakfast', 'Завтрак'),
    ('lunch', 'Обед'),
    ('dinner', 'Ужин'),
]


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ('recipe', 'ingredient', 'amount')


class RecipeForm(forms.ModelForm):
    tag = forms.MultipleChoiceField(
        required=False,
        choices=TAGS,
    )
    time = forms.IntegerField(min_value=1)

    class Meta:
        model = Recipe
        fields = ('name', 'image', 'description', 'tag', 'time')

    def __init__(self, *args, **kwargs):
        self.ingredients = []
        self.username = kwargs.pop('username')
        super(RecipeForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        for key, value in self.data.items():
            if key in ['breakfast', 'lunch', 'dinner']:
                cleaned_data['tag'].append(key)
            elif (key.startswith('nameIngredient')
                  or key.startswith('valueIngredient')):
                self.ingredients.append(value)

    def save(self, commit=True):
        recipe = super(RecipeForm, self).save(commit=False)
        recipe.author = self.username

        recipe.save()

        for i in range(0, len(self.ingredients), 2):
            ingredient = Ingredient.objects.get(title=self.ingredients[i])
            recipe_ingredient_form = RecipeIngredientForm(
                {
                    'recipe': recipe,
                    'ingredient': ingredient,
                    'amount': self.ingredients[i + 1]
                }
            )
            if recipe_ingredient_form.is_valid():
                recipe_ingredient_form.save()

        return recipe
