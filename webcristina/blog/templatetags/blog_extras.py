from django import template
from blog.models import Entrada_de_blog

register = template.Library()

@register.simple_tag
def get_entradas_de_blog():
    entradas_de_blog = Entrada_de_blog.objects.all()
    return entradas_de_blog

@register.simple_tag
def get_last_entradas_de_blog():
    last_entradas_de_blog = Entrada_de_blog.objects.order_by("-created")
    return last_entradas_de_blog
