from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeList(generic.ListView):
    model = Recipe
    template_name = "recipes/all_recipes.html"
    context_object_name = "recipes"