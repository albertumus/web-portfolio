from django.db import models

# Create your models here.

class Personalizacion(models.Model):
    title_menu = models.CharField(max_length=200, verbose_name="Título Menú")
    menu1 = models.CharField(max_length=200, verbose_name="Título Menú 1 ", null=True, blank=True)
    menu2 = models.CharField(max_length=200, verbose_name="Título Menú 2 ", null=True, blank=True)
    menu3 = models.CharField(max_length=200, verbose_name="Título Menú 3 ", null=True, blank=True)
    menu4 = models.CharField(max_length=200, verbose_name="Título Menú 4 ", null=True, blank=True)
    menu5 = models.CharField(max_length=200, verbose_name="Título Menú 5 ", null=True, blank=True)
    title_header = models.CharField(max_length=200, verbose_name="Título Header")
    subtitle_header = models.CharField(max_length=200, verbose_name="Subtítulo Header")
    button = models.CharField(max_length=200, verbose_name="Botón Header")
    title_service= models.CharField(max_length=200, verbose_name="Título Service")
    title_portfolio = models.CharField(max_length=200, verbose_name="Título Porfolio")
    title_cv = models.CharField(max_length=200, verbose_name="Título Sección CV")
    url_cv = models.URLField(max_length=200, verbose_name="URL CV")
    title_blog = models.CharField(max_length=200, verbose_name="Título Blog", null=True, blank=True)
    text_blog = models.CharField(max_length=200, verbose_name="Text Blog", null=True, blank=True)
    title_contact = models.CharField(max_length=200, verbose_name="Título Contact")
    text_contact = models.TextField(verbose_name="Texto Contact")
    phone = models.CharField(max_length=200, verbose_name="Teléfono")
    email = models.CharField(max_length=200, verbose_name="Título Header")

    class Meta:
        verbose_name = "Personalización Front-end"
        verbose_name_plural = "Personalizaciones"

    def __str__(self):
        return self.title_menu

class Servicios(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título del Servicio")
    text = models.CharField(max_length=200, verbose_name="Texto del Servicio")
    icon = models.CharField(max_length=200, verbose_name="Icono del Servicio")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    class Meta:
        verbose_name = "Servicios"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.title
        
