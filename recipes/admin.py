from django.contrib import admin
from .models import Recipe, Ingredient, Tag

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    list_filter = ("tags",)
    search_fields = ("name",)

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Tag)