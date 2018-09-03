from django.db import models

# Create your models here.

class ProjectCategory(models.Model):
        
        name = models.CharField(max_length=200, verbose_name="Nombre")
        created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
        updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

        class Meta:
            verbose_name = "categoria"
            verbose_name_plural = "catergorias"
            ordering = ["-created"]

        def __str__(self):
                return self.name
        

class Project(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion", null=True, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, null=True, blank=True)
    detail_date = models.CharField(max_length=200,verbose_name="Fecha", null=True, blank=True)
    detail_lugar = models.CharField(max_length=200,verbose_name="Lugar", null=True, blank=True)
    detail_productora = models.CharField(max_length=200,verbose_name="Productora", null=True, blank=True)
    detail_cliente = models.CharField(max_length=200,verbose_name="Cliente", null=True, blank=True)
    detail_software = models.CharField(max_length=500,verbose_name="Software", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="projects", null=False, blank=False)
    categories = models.ManyToManyField(ProjectCategory, verbose_name="Categoria", related_name="get_projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado" )
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


    class Meta:
            verbose_name = "projecto"
            verbose_name_plural = "projectos"
            ordering = ["created"]

    def __str__(self):
        return self.title