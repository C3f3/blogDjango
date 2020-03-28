from django.contrib import admin
from .models import Post

# Register your models here.
#registramos el modelo para que lo pueda reconocer el admin
admin.site.register(Post)