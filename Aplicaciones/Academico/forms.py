from django import forms
from .models import Producto
from .models import Cliente
from .models import Proveedor


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre', 'cantidad', 'descripcion', 'precio']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'apellido', 'telefono']
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['ruc', 'nombre', 'rubro', 'telefono']




from .models import Cliente, Producto

class VentaForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField(min_value=1)
