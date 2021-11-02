from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RecipeForm, IngredientForm
from django.views.generic import DetailView
from .models import Recipe, Ingredient, Association_Ingredient_Recipes
import re


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'books/index.html', {'recipes':recipes})

class RecipesDetailView(DetailView):
    model = Recipe
    template_name = 'books/details_view.html'
    context_object_name = 'recipes'

def create(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
        else:
            error = 'Incorrect form'

    form = RecipeForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'books/create.html', data)
# Create your views here.

def all_recipes(request):
    if request.method == "POST":
        searched_dishes = request.POST['recipe_or_name'].lower()
        searched_ingredients = re.split("[\s,\\+]*[\\+,\s,\\,]",request.POST['ingredients'].lower())
        searched_objects = Recipe.objects.all()
        searched = 0
        if searched_dishes:
            searched_objects = Recipe.objects.filter(name__contains= searched_dishes)
        searched = len(searched_ingredients)

        for word in searched_ingredients:
            if word == '':
                continue
            searched_objects = searched_objects.filter(ingredients__name__contains=word)
    return render(request, 'books/recipes.html', {'recipe_list':searched_objects,
                                                  'searched_dishes':searched_dishes,
                                                  'searched_ingredients': searched_ingredients,
                                                  'searched':searched,
                                                  })