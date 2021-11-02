from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Association_Ingredient_Recipes(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE,)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE,)

    def __str__(self):
        return self.recipe.name + " " + self.ingredient.name

class Recipe(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField('Recipe')
    date_added = models.DateTimeField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='Association_Ingredient_Recipes',
        through_fields=('recipe', 'ingredient'),
    )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipies'