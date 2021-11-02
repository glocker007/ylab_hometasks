from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Recipe, Ingredient, Association_Ingredient_Recipes
from .forms import RecipeForm
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Association_Ingredient_Recipes)