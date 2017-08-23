from django.contrib import admin
from .models import Material


class MaterialAdmin(admin.ModelAdmin):
     list_display = ["name","id", "brand_id","updated","timestamp"]
     class Meta:
         model=Material

admin.site.register(Material,MaterialAdmin)

# Register your models here.
