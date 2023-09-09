
from django.contrib import admin
from .models import Producto
from .models import Cliente
from .models import Venta

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)



