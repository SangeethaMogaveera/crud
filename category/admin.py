from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
     list_display = ["name","id","updated","timestamp"]
     class Meta:
         model=Category


admin.site.register(Category,CategoryAdmin)
