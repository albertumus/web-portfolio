from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Entrada_de_blog_category(models.Model):
    
        title = models.CharField(max_length=200, verbose_name="Título")
        created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
        updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

        class Meta:
            verbose_name = "categoria"
            verbose_name_plural = "catergorias"
            ordering = ["-created"]

        def __str__(self):
            return self.title

class Entrada_de_blog(models.Model):
    
        title = models.CharField(max_length=200, verbose_name="Título")
        content = RichTextField(verbose_name="Contenido")
        image = models.ImageField(upload_to="blog", verbose_name="Imagen")
        categories = models.ManyToManyField(Entrada_de_blog_category, verbose_name="Categorias", related_name="get_blogs")
        created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
        updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
    

        class Meta:
            verbose_name = "Entrada de Blog"
            verbose_name_plural = "Entradas de Blog"

        def __str__(self):
            return self.title


        
