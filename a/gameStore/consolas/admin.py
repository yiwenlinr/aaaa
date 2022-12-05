from django.contrib import admin
from  consolas.models import Proyecto

# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['tipo','marca','modelo','capacidad','peso','garantia']

admin.site.register(Proyecto)