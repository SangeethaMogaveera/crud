from django.contrib import admin
from .models import Po

def ordered(modeladmin, request, queryset):
    queryset.update(status='or')

def inprogress(modeladmin, request, queryset):
    queryset.update(status='in')

def partialdelivered(modeladmin, request, queryset):
    queryset.update(status='par')

def delivered(modeladmin, request, queryset):
    queryset.update(status='del')


class PoAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    actions = [ordered, inprogress, partialdelivered, delivered]
admin.site.register(Po,PoAdmin)

