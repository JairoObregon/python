from django.db import models

# Create your models here.
#Servicio
class servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descrpcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes', null=True,blank=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural= 'servicios'


#Usuario
class usuario(models.Model):
        Nombres = models.CharField(max_length=200)
        Apaterno = models.CharField(max_length=200)
        Amaterno= models.CharField(max_length=200)
        Edad= models.IntegerField()

        class Meta:
            verbose_name = 'usuario'
            verbose_name_plural= 'usuarios'