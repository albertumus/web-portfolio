from django import template
from portfolio.models import Project

register = template.Library()

@register.simple_tag
def get_project_list():
    projects = Project.objects.all()
    return projects
@register.simple_tag
def get_last_projects():
    projects = Project.objects.order_by("-created")
    return projects
