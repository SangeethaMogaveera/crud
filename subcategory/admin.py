from django.contrib import admin
from .models import Subcategory

class SubcategoryAdmin(admin.ModelAdmin):
     list_display = ["name","id", "cat_id","updated","timestamp"]
     class Meta:
         model=Subcategory

admin.site.register(Subcategory,SubcategoryAdmin)

# Register your models here.
