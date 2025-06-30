from django.db import models 

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    evento = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}, {self.evento}, {self.deporte}"
class Actividades(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length= 100)
    cultura = models.CharField(max_length=100)
    recreacion = models.CharField(max_length=100)
    unico = models.ManyToManyField(Entrenador)
    
    def __str__(self):
        return f"{self.nombre}, {self.deporte}, {self.cultura}, {self.recreacion}"
    
    
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    hora = models.DateField()
   
    
    def __str__(self):
        return f"{self.nombre} {self.tipo}, {self.deporte}, {self.hora}"
    

    
class Espacio(models.Model):
    cancha = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    disponible = models.BooleanField(True)
    uso = models.ForeignKey(Evento, on_delete=models.CASCADE)
    us = models.ManyToManyField(Actividades)


    def __str__(self):
        return f"{self.cancha}, {self.deporte}, {self.ubicacion}"

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    vario= models.ManyToManyField(Actividades)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}, {self.deporte}"
    
    
# Create your models here.
