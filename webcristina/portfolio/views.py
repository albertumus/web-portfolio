from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectCategory

# Create your views here.

def project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "portfolio/project.html", {"project":project})

def category(request, category_id):
    category = get_object_or_404(ProjectCategory, id=category_id)
    return render(request, "", {"category": category})