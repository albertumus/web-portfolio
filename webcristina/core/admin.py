from django.contrib import admin
from .models import Personalizacion, Servicios

# Register your models here.

class PersonalizacionAdmin(admin.ModelAdmin):
    readonly_fields = ()

admin.site.register(Personalizacion, PersonalizacionAdmin)

class ServiciosAdmin(admin.ModelAdmin):
    readonly_field = ["created", "updated"]

admin.site.register(Servicios, ServiciosAdmin)
    
