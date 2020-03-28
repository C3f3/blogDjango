from django.db import models
#modulo para manejo de fechas
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    #autor del post, clave foranea, hay que establecer la forma de eliminacio 
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    #titulo del post
    titulo = models.CharField(max_length = 200)
    #texto del post
    texto = models.TextField()
    #fecha de creacion del post, por defecto asigna la fecha actual
    fecha_creacion = models.DateTimeField(
        default = timezone.now
    )
    #fecha de publicacion, puede ser dejada en blanco
    fecha_publicacion = models.DateTimeField(blank=True,null = True)

    #metodo para cambiar el atributo para saber cuando sera publicado
    def publicar(self):
        self.fecha_publicacion = timezone.now()

    #forma en que van a mostrar cada objeto Post
    def __str__(self):
        return self.titulo
