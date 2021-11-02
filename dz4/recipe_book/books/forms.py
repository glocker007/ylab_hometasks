from .models import Recipe, Ingredient, Association_Ingredient_Recipes
from django.forms import ModelForm, TextInput,\
    DateTimeInput, ModelMultipleChoiceField, CheckboxSelectMultiple, Textarea

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields  = ["name", 'description', 'date_added', 'ingredients']
        ingredients = ModelMultipleChoiceField(queryset=Ingredient.objects.all())
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название рецепта',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание рецепта'
            }),
            "date_added": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата добавления'
            }),
            "ingredients": CheckboxSelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Ингридиенты'
            }),
        }

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']