from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Atraccion, Cliente, Boleto, RestTienda
from django.db import IntegrityError # Es útil para manejar errores de guardado

# ==============================================================
# FUNCIÓN PRINCIPAL FALTANTE (Causa del error)
# ==============================================================
def inicio_parque(request):
    """Muestra la página de inicio."""
    return render(request, 'inicio.html') # Asegúrate de que 'inicio.html' existe en app_parque/templates/

# ==============================================================
# FUNCIONES CRUD EMPLEADO
# ==============================================================

# Función: ver_empleado (Listar)
def ver_empleado(request):
    """Muestra la tabla de todos los empleados."""
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

# Función: agregar_empleado (Crear)
def agregar_empleado(request):
    atracciones = Atraccion.objects.all() # Necesario para el selector de FK

    if request.method == 'POST':
        try:
            id_atr_valor = request.POST.get('id_atr')
            # Busca la Atracción, o establece None si no se seleccionó
            atraccion_obj = get_object_or_404(Atraccion, pk=id_atr_valor) if id_atr_valor else None
            
            # Crear y guardar el objeto Empleado
            Empleado.objects.create(
                nombre=request.POST.get('nombre'),
                apellido=request.POST.get('apellido'),
                puesto=request.POST.get('puesto'),
                telefono=request.POST.get('telefono'),
                salario=request.POST.get('salario'),
                id_atr=atraccion_obj # Asignar el objeto Atraccion
            )
            return redirect('ver_empleado')
        except IntegrityError:
            return render(request, 'empleado/agregar_empleado.html', {'atracciones': atracciones, 'error_message': 'Error de integridad en los datos. Revise los campos.'})
        except Exception as e:
            return render(request, 'empleado/agregar_empleado.html', {'atracciones': atracciones, 'error_message': f'Error al guardar: {e}'})

    return render(request, 'empleado/agregar_empleado.html', {'atracciones': atracciones})

# Función: actualizar_empleado (Mostrar Formulario)
def actualizar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    atracciones = Atraccion.objects.all()
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado, 'atracciones': atracciones}) 

# Función: realizar_actualizacion_empleado (Guardar Cambios)
def realizar_actualizacion_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        id_atr_valor = request.POST.get('id_atr')
        atraccion_obj = get_object_or_404(Atraccion, pk=id_atr_valor) if id_atr_valor else None

        # Actualizar campos
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.puesto = request.POST.get('puesto')
        empleado.telefono = request.POST.get('telefono')
        empleado.salario = request.POST.get('salario')
        empleado.id_atr = atraccion_obj

        empleado.save()
        return redirect('ver_empleado')
    return redirect('ver_empleado')

# Función: borrar_empleado (Eliminar)
def borrar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    
    # Vista de confirmación (si es GET)
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})
# ... (Mantener todo el código de Empleado existente) ...

# ==============================================================
# FUNCIONES CRUD ATRACCIÓN (Relación con Empleado)
# ==============================================================

# Función: ver_atraccion (Listar)
def ver_atraccion(request):
    """Muestra la tabla de todas las atracciones."""
    atracciones = Atraccion.objects.all()
    # Para el listado, podemos acceder al nombre del empleado encargado: atraccion.id_emp.nombre
    return render(request, 'atraccion/ver_atraccion.html', {'atracciones': atracciones})

# Función: agregar_atraccion (Crear)
def agregar_atraccion(request):
    # Necesario para el desplegable: obtener todos los empleados (posibles encargados)
    empleados = Empleado.objects.all() 
    
    if request.method == 'POST':
        try:
            id_emp_valor = request.POST.get('id_emp')
            # Busca el Empleado, o establece None si no se seleccionó
            empleado_obj = get_object_or_404(Empleado, pk=id_emp_valor) if id_emp_valor else None
            
            Atraccion.objects.create(
                nombre=request.POST.get('nombre'),
                tipo=request.POST.get('tipo'),
                capacidad=request.POST.get('capacidad'),
                estado=request.POST.get('estado'),
                altura_min=request.POST.get('altura_min'),
                id_emp=empleado_obj # Asignar el objeto Empleado (FK)
            )
            return redirect('ver_atraccion')
        except Exception as e:
            return render(request, 'atraccion/agregar_atraccion.html', {'empleados': empleados, 'error_message': f'Error al guardar la atracción: {e}'})

    return render(request, 'atraccion/agregar_atraccion.html', {'empleados': empleados})

# Función: actualizar_atraccion (Mostrar Formulario)
def actualizar_atraccion(request, pk):
    atraccion = get_object_or_404(Atraccion, pk=pk)
    empleados = Empleado.objects.all()
    return render(request, 'atraccion/actualizar_atraccion.html', {'atraccion': atraccion, 'empleados': empleados})

# Función: realizar_actualizacion_atraccion (Guardar Cambios)
def realizar_actualizacion_atraccion(request, pk):
    atraccion = get_object_or_404(Atraccion, pk=pk)
    if request.method == 'POST':
        id_emp_valor = request.POST.get('id_emp')
        empleado_obj = get_object_or_404(Empleado, pk=id_emp_valor) if id_emp_valor else None

        atraccion.nombre = request.POST.get('nombre')
        atraccion.tipo = request.POST.get('tipo')
        atraccion.capacidad = request.POST.get('capacidad')
        atraccion.estado = request.POST.get('estado')
        atraccion.altura_min = request.POST.get('altura_min')
        atraccion.id_emp = empleado_obj

        atraccion.save()
        return redirect('ver_atraccion')
    return redirect('ver_atraccion')

# Función: borrar_atraccion (Eliminar)
def borrar_atraccion(request, pk):
    atraccion = get_object_or_404(Atraccion, pk=pk)
    if request.method == 'POST':
        atraccion.delete()
        return redirect('ver_atraccion')
    return render(request, 'atraccion/borrar_atraccion.html', {'atraccion': atraccion})


# ==============================================================
# FUNCIONES CRUD CLIENTE (Relación con Atracción)
# ==============================================================

# Función: ver_cliente (Listar)
def ver_cliente(request):
    """Muestra la tabla de todos los clientes."""
    clientes = Cliente.objects.all()
    # Para el listado, accedemos al nombre de la atracción: cliente.id_atr.nombre
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

# Función: agregar_cliente (Crear)
def agregar_cliente(request):
    # Necesario para el desplegable: obtener todas las atracciones
    atracciones = Atraccion.objects.all() 
    
    if request.method == 'POST':
        try:
            id_atr_valor = request.POST.get('id_atr')
            # La relación con Cliente debe ser CASCADE, así que el valor debe existir
            atraccion_obj = get_object_or_404(Atraccion, pk=id_atr_valor) if id_atr_valor else None
            
            Cliente.objects.create(
                nombre=request.POST.get('nombre'),
                apellido=request.POST.get('apellido'),
                telefono=request.POST.get('telefono'),
                correo=request.POST.get('correo'),
                # fecha_reg se autocompleta con auto_now_add=True
                id_atr=atraccion_obj # Asignar el objeto Atraccion (FK)
            )
            return redirect('ver_cliente')
        except Exception as e:
            return render(request, 'cliente/agregar_cliente.html', {'atracciones': atracciones, 'error_message': f'Error al guardar el cliente: {e}'})

    return render(request, 'cliente/agregar_cliente.html', {'atracciones': atracciones})

# Función: actualizar_cliente (Mostrar Formulario)
def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    atracciones = Atraccion.objects.all()
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente, 'atracciones': atracciones})

# Función: realizar_actualizacion_cliente (Guardar Cambios)
def realizar_actualizacion_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        id_atr_valor = request.POST.get('id_atr')
        atraccion_obj = get_object_or_404(Atraccion, pk=id_atr_valor) if id_atr_valor else None

        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.correo = request.POST.get('correo')
        # La fecha de registro no se actualiza
        cliente.id_atr = atraccion_obj

        cliente.save()
        return redirect('ver_cliente')
    return redirect('ver_cliente')

# Función: borrar_cliente (Eliminar)
def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ... (código existente para Empleado, Atracción, Cliente) ...

# ==============================================================
# FUNCIONES CRUD BOLETO
# ==============================================================

# Función: ver_boleto (Listar)
def ver_boleto(request):
    boletos = Boleto.objects.all()
    return render(request, 'boleto/ver_boleto.html', {'boletos': boletos})

# Función: agregar_boleto (Crear)
def agregar_boleto(request):
    if request.method == 'POST':
        try:
            Boleto.objects.create(
                tipo=request.POST.get('tipo'),
                precio=request.POST.get('precio'),
                fecha_com=request.POST.get('fecha_com'),
                metodo_pago=request.POST.get('metodo_pago'),
            )
            return redirect('ver_boleto')
        except Exception as e:
            return render(request, 'boleto/agregar_boleto.html', {'error_message': f'Error al guardar el boleto: {e}'})

    return render(request, 'boleto/agregar_boleto.html')

# Función: actualizar_boleto (Mostrar Formulario)
def actualizar_boleto(request, pk):
    boleto = get_object_or_404(Boleto, pk=pk)
    return render(request, 'boleto/actualizar_boleto.html', {'boleto': boleto})

# Función: realizar_actualizacion_boleto (Guardar Cambios)
def realizar_actualizacion_boleto(request, pk):
    boleto = get_object_or_404(Boleto, pk=pk)
    if request.method == 'POST':
        boleto.tipo = request.POST.get('tipo')
        boleto.precio = request.POST.get('precio')
        boleto.fecha_com = request.POST.get('fecha_com')
        boleto.metodo_pago = request.POST.get('metodo_pago')
        boleto.save()
        return redirect('ver_boleto')
    return redirect('ver_boleto')

# Función: borrar_boleto (Eliminar)
def borrar_boleto(request, pk):
    boleto = get_object_or_404(Boleto, pk=pk)
    if request.method == 'POST':
        boleto.delete()
        return redirect('ver_boleto')
    return render(request, 'boleto/borrar_boleto.html', {'boleto': boleto})


# ==============================================================
# FUNCIONES CRUD TIENDAS Y RESTAURANTES (RestTienda con FK a Empleado)
# ==============================================================

# Función: ver_resttienda (Listar)
def ver_resttienda(request):
    resttiendas = RestTienda.objects.all()
    return render(request, 'resttienda/ver_resttienda.html', {'resttiendas': resttiendas})

# Función: agregar_resttienda (Crear)
def agregar_resttienda(request):
    empleados = Empleado.objects.all() # Necesario para el selector de FK
    
    if request.method == 'POST':
        try:
            id_emp_valor = request.POST.get('id_emp')
            empleado_obj = get_object_or_404(Empleado, pk=id_emp_valor) if id_emp_valor else None
            
            RestTienda.objects.create(
                nombre=request.POST.get('nombre'),
                tipo=request.POST.get('tipo'),
                ubicacion=request.POST.get('ubicacion'),
                horario=request.POST.get('horario'),
                id_emp=empleado_obj # Asignar el objeto Empleado (FK)
            )
            return redirect('ver_resttienda')
        except Exception as e:
            return render(request, 'resttienda/agregar_resttienda.html', {'empleados': empleados, 'error_message': f'Error al guardar el local: {e}'})

    return render(request, 'resttienda/agregar_resttienda.html', {'empleados': empleados})

# Función: actualizar_resttienda (Mostrar Formulario)
def actualizar_resttienda(request, pk):
    resttienda = get_object_or_404(RestTienda, pk=pk)
    empleados = Empleado.objects.all()
    return render(request, 'resttienda/actualizar_resttienda.html', {'resttienda': resttienda, 'empleados': empleados})

# Función: realizar_actualizacion_resttienda (Guardar Cambios)
def realizar_actualizacion_resttienda(request, pk):
    resttienda = get_object_or_404(RestTienda, pk=pk)
    if request.method == 'POST':
        id_emp_valor = request.POST.get('id_emp')
        empleado_obj = get_object_or_404(Empleado, pk=id_emp_valor) if id_emp_valor else None

        resttienda.nombre = request.POST.get('nombre')
        resttienda.tipo = request.POST.get('tipo')
        resttienda.ubicacion = request.POST.get('ubicacion')
        resttienda.horario = request.POST.get('horario')
        resttienda.id_emp = empleado_obj

        resttienda.save()
        return redirect('ver_resttienda')
    return redirect('ver_resttienda')

# Función: borrar_resttienda (Eliminar)
def borrar_resttienda(request, pk):
    resttienda = get_object_or_404(RestTienda, pk=pk)
    if request.method == 'POST':
        resttienda.delete()
        return redirect('ver_resttienda')
    return render(request, 'resttienda/borrar_resttienda.html', {'resttienda': resttienda})