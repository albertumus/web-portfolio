from django.contrib import admin
from .models import Project, ProjectCategory

# Register your models here.

class ProjectCategoryAdmin(admin.ModelAdmin):
    readonly_field = ("created", "updated")

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
