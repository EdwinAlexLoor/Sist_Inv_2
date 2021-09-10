from django.db import models

# Create your models here.
class bodega (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=256)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta:
        db_table = 'tp_bodega'

class Categoria_producto ( models.Model ) :
    nombre = models.CharField ( max_length= 50 )
    descripcion = models.CharField ( max_length=256)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = 'tp_categoria_producto'


class Marca (models.Model):
    nombre = models.CharField(max_length=50)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = 'tp_marca'


class unidad_medida (models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.CharField(max_length=100)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_unidad_medida'

class rol_persona (models.Model):
    cargo = models.CharField(max_length=50)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_rol_persona'
        verbose_name = "Rol Persona"
        verbose_name_plural = "Roles De Personas"

    def __str__(self):
        return "{}".format(self.cargo)


class ingreso_cabecera (models.Model):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)

    class Meta :
        db_table = 'tp_ingreso_cabecera'


class Egreso_cabecera ( models.Model ) :
    codigo = models.CharField ( max_length= 50 )
    descripcion = models.CharField ( max_length=256)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = 'tp_egreso_cabecera'

class Persona (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    direccion = models.CharField(max_length=250)
    cedula =models.CharField(max_length=10)
    correo =models.EmailField(null= True, blank= True)
    Rol_persona = models.ForeignKey(rol_persona, on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default= 1)

    class Meta:
        db_table = 'tp_persona'
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return "{}{}{} ".format(self.nombre, "    ", self.apellido)



class producto (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_producto'

class Devolucion ( models.Model ) :
    detalle = models.CharField ( max_length= 256 )


    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = 'tp_devolucion'

class proveedor (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    direccion = models.CharField(max_length=250)
    celular = models.CharField(max_length=10)
    correo = models.EmailField(null= True, blank= True)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = 'tp_proveedor'



class Bodega_producto (models.Model):
    cantidad = models.CharField(max_length= 5)
    unidad  = models.CharField(max_length=10)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default= 1)

    class Meta:
        db_table = 'tp_bodega_producto'



class ingreso_detalle (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_ingreso_detalle'


class Egreso_detalle ( models.Model ) :
    cantidad = models.CharField(max_length= 50)
    precio = models.CharField(max_length=5)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = 'tp_egreso_detalle'