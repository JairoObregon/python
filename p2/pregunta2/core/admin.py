from django.contrib import admin
from .models import usuario,servicio
# Register your models here.

class Servicio(admin.ModelAdmin):
    list_display = ('id','nombre' )

class Usuario(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(usuario,Usuario)
admin.site.register(servicio,Servicio)