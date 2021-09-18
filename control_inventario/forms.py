from django.forms import ModelForm
from .models import Persona, bodega, Bodega_producto, Categoria_producto, Devolucion, Egreso_detalle, \
    Egreso_cabecera, Marca , rol_persona, ingreso_cabecera, ingreso_detalle, producto, proveedor, CategoriaBodega

class Categoria_bodegaForm (ModelForm):
    class Meta:
        model = CategoriaBodega
        fields = ['nombre', 'descripcion' ]

class BodegaForm (ModelForm):
    class Meta:
        model = bodega
        fields = ['nombre', 'descripcion' ]


class Categoria_productoForm (ModelForm):
    class Meta:
        model = Categoria_producto
        fields = ['nombre', 'descripcion' ]


class MarcaForm (ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']


class Rol_personaForm(ModelForm):
    class Meta:
        model = rol_persona
        fields = ['cargo']



class Ingreso_cabeceraForm (ModelForm):
    class Meta:
        model = ingreso_cabecera
        fields = ['codigo_documento', 'fecha_documento', 'usuario_recibe', 'usuario_entrega', 'total_ingreso' ]


class Egreso_cabeceraForm (ModelForm):
    class Meta:
        model = Egreso_cabecera
        fields = ['codigo_documento', 'fecha_documento', 'usuario_entrega', 'usuario_recibe', 'total_egreso' ]


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'cedula', 'correo', 'Rol_persona' ]


class ProductoForm (ModelForm):
    class Meta:
        model = producto
        fields = [ 'codigo', 'nombre', 'descripcion', 'categoria_producto' ]

class DevolucionForm (ModelForm):
    class Meta:
        model = Devolucion
        fields = ['detalle' ]


class ProveedorForm (ModelForm):
    class Meta:
        model = proveedor
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'celular', 'correo' ]


class Bodega_productoForm (ModelForm):
    class Meta:
        model = Bodega_producto
        fields = ['Bodega', 'Producto', 'cantidad_existencia', 'precio_compra', 'precio_venta', 'stock_maximo', 'stock_minimo' ]


class Ingreso_detalleForm (ModelForm):
    class Meta:
        model = ingreso_detalle
        fields = ['Ingreso_cabecera', 'Producto', 'cantidad_ingreso', 'precio_ingreso', 'sub_total' ]

class Egreso_detalleForm (ModelForm):
    class Meta:
        model = Egreso_detalle
        fields = ['egreso_cabecera', 'Producto', 'cantidad_egreso', 'precio_egreso', 'sub_total']








