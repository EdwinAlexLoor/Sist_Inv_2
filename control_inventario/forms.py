from django.forms import ModelForm
from .models import Persona, bodega, Bodega_producto, Categoria_producto, Devolucion, Egreso_detalle, Egreso_cabecera, Marca , unidad_medida, rol_persona, ingreso_cabecera, ingreso_detalle, producto, proveedor

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'cedula', 'correo', 'Rol_persona' ]


class BodegaForm (ModelForm):
    class Meta:
        model = bodega
        fields = ['nombre', 'descripcion' ]

class Bodega_productoForm (ModelForm):
    class Meta:
        model = Bodega_producto
        fields = ['cantidad', 'unidad' ]

class Categoria_productoForm (ModelForm):
    class Meta:
        model = Categoria_producto
        fields = ['nombre', 'descripcion' ]

class DevolucionForm (ModelForm):
    class Meta:
        model = Devolucion
        fields = ['detalle' ]


class Egreso_detalleForm (ModelForm):
    class Meta:
        model = Egreso_detalle
        fields = ['cantidad', 'precio' ]

class Egreso_cabeceraForm (ModelForm):
    class Meta:
        model = Egreso_cabecera
        fields = ['codigo', 'descripcion' ]


class MarcaForm (ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class Unidad_medidaForm(ModelForm):
    class Meta:
        model = unidad_medida
        fields = ['nombre', 'medida']

class Rol_personaForm(ModelForm):
    class Meta:
        model = rol_persona
        fields = ['cargo']

class Ingreso_cabeceraForm (ModelForm):
    class Meta:
        model = ingreso_cabecera
        fields = ['codigo', 'descripcion' ]

class Ingreso_detalleForm (ModelForm):
    class Meta:
        model = ingreso_detalle
        fields = ['nombre', 'descripcion' ]

class ProductoForm (ModelForm):
    class Meta:
        model = producto
        fields = ['nombre', 'descripcion' ]

class ProveedorForm (ModelForm):
    class Meta:
        model = proveedor
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'celular', 'correo' ]
