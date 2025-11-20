from django.urls import path
from . import views

urlpatterns = [
    # Principal
    path('', views.inicio_parque, name='inicio_parque'),
    
    # --------------------------------------------------
    # CRUD de EMPLEADO (Ya creado, solo se incluye)
    # --------------------------------------------------
    path('empleado/', views.ver_empleado, name='ver_empleado'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:pk>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:pk>/', views.borrar_empleado, name='borrar_empleado'),

    # --------------------------------------------------
    # CRUD de ATRACCIÓN
    # --------------------------------------------------
    path('atraccion/', views.ver_atraccion, name='ver_atraccion'),
    path('atraccion/agregar/', views.agregar_atraccion, name='agregar_atraccion'),
    path('atraccion/actualizar/<int:pk>/', views.actualizar_atraccion, name='actualizar_atraccion'),
    path('atraccion/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_atraccion, name='realizar_actualizacion_atraccion'),
    path('atraccion/borrar/<int:pk>/', views.borrar_atraccion, name='borrar_atraccion'),

    # --------------------------------------------------
    # CRUD de CLIENTE
    # --------------------------------------------------
    path('cliente/', views.ver_cliente, name='ver_cliente'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    # --------------------------------------------------
    # CRUD de BOLETO (NUEVO)
    # --------------------------------------------------
    path('boleto/', views.ver_boleto, name='ver_boleto'),
    path('boleto/agregar/', views.agregar_boleto, name='agregar_boleto'),
    path('boleto/actualizar/<int:pk>/', views.actualizar_boleto, name='actualizar_boleto'),
    path('boleto/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_boleto, name='realizar_actualizacion_boleto'),
    path('boleto/borrar/<int:pk>/', views.borrar_boleto, name='borrar_boleto'),

    # --------------------------------------------------
    # CRUD de TIENDAS/RESTAURANTES (NUEVO)
    # --------------------------------------------------
    path('resttienda/', views.ver_resttienda, name='ver_resttienda'),
    path('resttienda/agregar/', views.agregar_resttienda, name='agregar_resttienda'),
    path('resttienda/actualizar/<int:pk>/', views.actualizar_resttienda, name='actualizar_resttienda'),
    path('resttienda/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_resttienda, name='realizar_actualizacion_resttienda'),
    path('resttienda/borrar/<int:pk>/', views.borrar_resttienda, name='borrar_resttienda'),
]