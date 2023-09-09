from django.views.decorators.csrf import csrf_protect
from .models import Cliente
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ProductoForm
from .models import Producto
from collections import Counter
import plotly.express as px
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ClienteForm
from .models import Proveedor
from django.views import View
from django.db.models import F
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductoForm
from django.http import JsonResponse
from .models import Cliente, Producto
from .forms import VentaForm  # Adjust the import path based on your project structure.

#Grafico de barras
def grafica_barras(request):
    productos = Producto.objects.all()

    # Crea un DataFrame de pandas con los datos de los productos
    data = {
        'nombre': [producto.nombre for producto in productos],
        'cantidad': [producto.cantidad for producto in productos],
    }

    # Crea un gráfico de barras interactivas con Plotly
    fig = px.bar(data, x='nombre', y='cantidad', title='Cantidad de Productos')

    # Convierte el gráfico de Plotly en JSON
    graph_json = fig.to_json()

    context = {
        'graph_json': graph_json,
    }

    return render(request, 'inicio.html', context)


import plotly.express as px
from django.shortcuts import render
from .models import Venta, Producto

import plotly.express as px
from django.shortcuts import render
from .models import Venta

def ventas_por_dia(request):
    # Obtener los datos de ventas por día
    ventas_por_dia = Venta.objects.values('fecha').annotate(total_ventas=models.Sum('cantidad')).order_by('fecha')

    # Crear un DataFrame para usar con Plotly
    import pandas as pd
    df = pd.DataFrame(list(ventas_por_dia))

    # Generar la gráfica
    fig = px.line(df, x='fecha', y='total_ventas', title='Ventas por día')
    graph = fig.to_html(full_html=False)

    return render(request, 'inicio.html', {'graph': graph})

#Vista del inventario
#Listar los productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestionProductos.html', {'productos': productos})

#Agregar productos


from django.contrib import messages
from .models import Producto  # Asegúrate de importar el modelo Producto adecuadamente

def registrar_producto(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        cantidad = request.POST['txtCantidad']
        descripcion = request.POST['txtDescripcion']
        precio = request.POST['txtPrecio']

        # Crea un nuevo producto en la base de datos
        producto = Producto.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad, descripcion=descripcion, precio=precio)
        messages.success(request, '¡Producto registrado!')

        return redirect('/inventario/')  # Asegúrate de que esta URL esté configurada correctamente en tus archivos de rutas

    return render(request, 'venta.html')  # Reemplaza 'tu_template.html' con la plantilla que estás usando para el formulario






#Eliminar producto
def eliminar_producto(request, codigo):
    try:
        producto = Producto.objects.get(codigo=codigo)
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
    except Producto.DoesNotExist:
        # Manejar el caso en el que el producto no existe
        messages.error(request, 'El producto no existe.')

    # Redirige a la página donde se muestra la lista de productos actualizada
    return redirect('lista_productos')
#Editar productos formulario
def edicion_producto(request, codigo):
    producto =Producto.objects.get(codigo=codigo)
    return render(request, "edicionProductos.html", {"producto": producto})
#Editar productos acción
def editar_producto(request, codigo):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        cantidad = request.POST['txtCantidad']
        descripcion = request.POST['txtDescripcion']
        precio = request.POST['txtPrecio']

        producto = Producto.objects.get(codigo=codigo)
        producto.nombre = nombre
        producto.cantidad = cantidad
        producto.descripcion = descripcion
        producto.precio = precio
        producto.save()

        messages.success(request, '¡Producto actualizado!')
        return redirect('/inventario/')

    else:
        producto = Producto.objects.get(codigo=codigo)
        return render(request, "edicionProductos.html", {"producto": producto})



#Vista del Clientes
#Listar cliente
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestionClientes.html', {'clientes': clientes})

#Registrar cliente
def registrar_cliente(request):
    dni = request.POST['txtDNI']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    cliente = Cliente.objects.create(dni=dni, nombre=nombre, apellido=apellido, telefono=telefono)
    messages.success(request, '¡Cliente registrado!')

    return redirect('/cliente/')
#Eliminar cliente
def eliminar_cliente(request, dni):
    cliente = Cliente.objects.get(dni=dni)
    cliente.delete()
    messages.success(request, '¡Cliente eliminado!')
    return redirect('lista_clientes')
#Editar cliente formulario
def edicion_cliente(request, dni):
    cliente = Cliente.objects.get(dni=dni)
    return render(request, "edicionClientes.html", {"cliente": cliente})
#Editar cliente acción
def editar_cliente(request, dni):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        telefono = request.POST['txtTelefono']

        cliente = Cliente.objects.get(dni=dni)
        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.telefono = telefono
        cliente.save()

        messages.success(request, '¡Cliente actualizado!')
        return redirect('/cliente/')

    else:
        cliente = Cliente.objects.get(dni=dni)
        return render(request, "edicionClientes.html", {"cliente": cliente})


# Vista de proveedores
#Lista proveedores
def lista_proveedores(request):
    listaProveedores = Proveedor.objects.all()
    return render(request, "gestionProveedores.html", {"proveedores":listaProveedores})

#Registrar proveedor
def registrar_proveedor(request):
    if request.method == 'POST':
        ruc = request.POST.get('txtRUC')
        nombre = request.POST.get('txtNombre')
        rubro = request.POST.get('txtRubro')
        telefono = request.POST.get('txtTelefono')

        try:
            proveedor = Proveedor.objects.create(ruc=ruc, nombre=nombre, rubro=rubro, telefono=telefono)
            messages.success(request, '¡Proveedor registrado!')
            return redirect('lista_proveedores')  
        except Exception as e:
            messages.error(request, f'Error al registrar proveedor: {str(e)}')

    return render(request, 'gestionProveedores.html')



#Eliminar proveedor
def eliminar_proveedor(request, ruc):
    proveedor = Proveedor.objects.get(ruc=ruc)
    proveedor.delete()
    messages.success(request, '¡Proveedor eliminado!')
    return redirect('lista_proveedores')

#Editar proveedor formulario
def edicion_proveedor(request, ruc):
    proveedor =Proveedor.objects.get(ruc=ruc)
    return render(request, "edicionProveedores.html", {"proveedor": proveedor})
#Editar proveedor acción
def editar_proveedor(request, ruc):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        rubro = request.POST['txtRubro']
        telefono = request.POST['txtTelefono']

        proveedor = Proveedor.objects.get(ruc=ruc)
        proveedor.nombre = nombre
        proveedor.rubro = rubro
        proveedor.telefono = telefono
        proveedor.save()

        messages.success(request, '¡Proveedor actualizado!')
        return redirect('/proveedor/')

    else:
        proveedor = Proveedor.objects.get(ruc=ruc)
        return render(request, "edicionProveedores.html", {"proveedor": proveedor})

#VENTA
from django.shortcuts import render, redirect
from .models import Venta

def realizar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']

            if cantidad <= producto.cantidad:
                venta = Venta(cliente=cliente, producto=producto, cantidad=cantidad)
                venta.save()

                # Disminuir la cantidad de stock
                producto.cantidad -= cantidad
                producto.save()

                return render(request, 'detalleVenta.html', {'venta': venta})
            else:
                error_msg = "No hay suficiente stock disponible."
        else:
            error_msg = "Formulario no válido. Por favor, verifique los datos."

    else:
        form = VentaForm()
        error_msg = None

    return render(request, 'venta.html', {'form': form, 'error_msg': error_msg})


from django.shortcuts import render
from .models import Venta
from django.db.models import Q

def listar_ventas(request):
    ventas = Venta.objects.all()
    query = request.GET.get('q')
    if query:
        ventas = ventas.filter(
            Q(cliente__nombre__icontains=query) |
            Q(producto__nombre__icontains=query)
        )
    return render(request, 'listaVentas.html', {'ventas': ventas})

#LOGIN
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('grafica_barras')  
        else:
            pass

    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('login')