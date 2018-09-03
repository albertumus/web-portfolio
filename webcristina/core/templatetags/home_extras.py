from django import template
from core.models import Personalizacion

register = template.Library()

@register.simple_tag
def get_personalizacion():
    personalizacion= Personalizacion.objects.all()
    return personalizacion
 