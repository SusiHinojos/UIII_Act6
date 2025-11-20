from django.contrib import admin
from .models import Empleado, Cliente, Atraccion, Boleto, RestTienda

# Registrar los tres modelos
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Atraccion)
admin.site.register(Boleto)      # <-- REGISTRAR
admin.site.register(RestTienda)