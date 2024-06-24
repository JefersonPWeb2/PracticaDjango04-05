from django.db import models
from django.urls import reverse
# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField(blank=True)
    donador = models.BooleanField()
    
    def get_absolute_url(self):
        return reverse('personas:persona-detail', kwargs = {'pk': self.id})