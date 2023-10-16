from django.contrib import admin
from .models import recipes

# Register your models here.

class recipeAdmin(admin.ModelAdmin):
    class Meta:
        model = recipes
        fields = '__all__'


admin.site.register(recipes, recipeAdmin)