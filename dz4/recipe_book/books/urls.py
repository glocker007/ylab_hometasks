from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='recipe_list'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.RecipesDetailView.as_view(), name='recipes'),
    path('recipes/', views.all_recipes, name='recipes_list'),
]