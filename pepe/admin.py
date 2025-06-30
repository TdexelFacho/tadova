from django.contrib import admin

from apps.pepe.models import Entrenador, Actividades, Evento, Socio

admin.site.register(Entrenador)
admin.site.register(Actividades)
admin.site.register(Evento)
admin.site.register(Socio)
# Register your models here.
