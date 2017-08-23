from django.contrib import admin
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ["name","id","sub_cat_id","updated","timestamp"]
    class Meta:
        model=Brand



admin.site.register(Brand,BrandAdmin)

# Register your models here.
