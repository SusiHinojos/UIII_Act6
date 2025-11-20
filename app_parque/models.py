from django.db import models

# NOTA: Atraccion y Empleado se definen con ForeignKey circular (ambos se referencian). 
# Para evitar errores de referencia, Atraccion debe definirse primero, o usar cadena. 
# Aquí usaremos la cadena 'Atraccion' en Empleado para asegurar la funcionalidad.

# =================
# MODELO: ATRACCIÓN
# =================
class Atraccion(models.Model):
    # Clave Primaria (PK)
    id_atr = models.AutoField(primary_key=True, unique=True) # [cite: 53]

    # Campos
    nombre = models.CharField(max_length=50) # [cite: 54]
    tipo = models.CharField(max_length=50) # [cite: 55]
    capacidad = models.IntegerField() # [cite: 56]
    estado = models.CharField(max_length=100) # [cite: 57]
    altura_min = models.DecimalField(max_digits=3, decimal_places=2) # [cite: 58]

    # Clave Foránea (FK) a Empleado (Empleado encargado de la Atracción)
    # Se usa SET_NULL para que si se borra el Empleado, la Atracción no se borre.
    id_emp = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True, blank=True) # [cite: 59]

    def __str__(self):
        return self.nombre # [cite: 61]
    
# =================
# MODELO: EMPLEADO (Trabajaremos con este primero, como se indica en el paso 13)
# =================
class Empleado(models.Model):
    # Clave Primaria (PK)
    id_emp = models.AutoField(primary_key=True, unique=True) # [cite: 28]

    # Campos
    nombre = models.CharField(max_length=50) # [cite: 29]
    apellido = models.CharField(max_length=50) # [cite: 30]
    puesto = models.CharField(max_length=40) # 
    telefono = models.CharField(max_length=15) # [cite: 32]
    salario = models.DecimalField(max_digits=8, decimal_places=2) # [cite: 33]
    
    # Clave Foránea (FK) a Atraccion (Atracción asignada al Empleado)
    # id_atr: La FK se define en el modelo Empleado.
    id_atr = models.ForeignKey(Atraccion, on_delete=models.SET_NULL, null=True, blank=True) # [cite: 34]
    
    def __str__(self):
        return self.nombre # [cite: 35, 36]

# =================
# MODELO: CLIENTE
# =================

class Cliente(models.Model):
    id_cli = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    
    # NUEVO CAMPO: Clave Foránea a Boleto
    # on_delete=models.SET_NULL permite que si se borra el boleto, el cliente no se borre
    id_bol = models.ForeignKey('Boleto', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
# =================
# MODELO: BOLETO
# =================
class Boleto(models.Model):
    id_bol = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_com = models.DateField()
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Boleto {self.id_bol} - {self.tipo}"

# =================
# MODELO: RESTAURANTE/TIENDA (RestTienda)
# =================
class RestTienda(models.Model):
    id_local = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30) # Ej. Restaurante, Tienda de Souvenirs
    ubicacion = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    
    # Clave Foránea (FK) a Empleado (Empleado encargado del local)
    id_emp = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre