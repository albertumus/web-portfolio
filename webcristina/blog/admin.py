from django.contrib import admin
from .models import Entrada_de_blog, Entrada_de_blog_category

# Register your models here.

class Entrada_de_blogAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class Entrada_de_blog_categoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    ordering = ["created"]
    list_display = ("title", "created")
    date_hierarchy = "created"

    class Media:
        css = {
            'all': ('blog/css/custom_ckeditor.css',)
        }    

admin.site.register(Entrada_de_blog, Entrada_de_blogAdmin)
admin.site.register(Entrada_de_blog_category, Entrada_de_blog_categoryAdmin)

