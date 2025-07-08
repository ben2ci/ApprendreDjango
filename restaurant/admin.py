from django.contrib import admin
from .models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "available")

    search_fields = ("name", "description", "price", "available")

# Register your models here.
# admin.site.register(Meal)
