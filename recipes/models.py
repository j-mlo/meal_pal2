from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    """
    Model for tag used to categorise a recipe
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Ingredient(models.Model):
    """
    Model for ingredients used in recipes
    """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    """
    Model for recipe
    """
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="recipes/", null=True, blank=True)
    prep_time = models.DurationField(null=True, blank=True)
    cooking_time = models.DurationField(null=True, blank=True)
    serving = models.PositiveIntegerField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes", blank=True)
    method = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="recipes", blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="recipes", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

