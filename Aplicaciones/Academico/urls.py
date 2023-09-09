
from django.urls import path
from . import views

urlpatterns = [
    #Login
    path('', views.login_view, name='login'),  
    path('logout/', views.signout, name='logout'),
    #Inventario
    path('grafica_barras', views.grafica_barras, name='grafica_barras'),
    path('inventario/', views.lista_productos, name='lista_productos'),
    path('registrar_producto/', views.registrar_producto, name='registrar_producto'),
    path('editar_producto/<str:codigo>/', views.edicion_producto, name='edicion_producto'),
    path('actualizar_producto/<str:codigo>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<str:codigo>/', views.eliminar_producto, name='eliminar_producto'),
    #Clientes
    path('cliente/', views.lista_clientes, name='lista_clientes'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('editar_cliente/<int:dni>/', views.edicion_cliente, name='edicion_cliente'),
    path('actualizar_cliente/<int:dni>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:dni>/', views.eliminar_cliente, name='eliminar_cliente'),
    #Proveedores
    path('proveedor/', views.lista_proveedores, name='lista_proveedores'),
    path('registrar_proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('editar_proveedor/<int:ruc>/', views.edicion_proveedor, name='edicion_proveedor'),
    path('actualizar_proveedor/<int:ruc>/', views.editar_proveedor, name='editar_proveedor'), 
    path('eliminar_proveedor/<int:ruc>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    #Ventas
    path('realizar_venta/', views.realizar_venta, name='realizar_venta'),
    path('lista_ventas/', views.listar_ventas, name='listar_ventas'),

]


