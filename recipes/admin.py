# отредачено
from django.contrib import admin
from .models import Recipe, Category

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image') 

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)




