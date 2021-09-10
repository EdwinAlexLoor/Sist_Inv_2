from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from .forms import PersonaForm , BodegaForm, Rol_personaForm
from .models import Persona, rol_persona


# Create your views here.
def saludo( request ) :
    return HttpResponse ( "Hola Mundo" )


def index( request ) :
    return render ( request , "index.html" )


#def MiPrimeraFuncion( request ) :
   # return render ( request , "base.html" )

def base2 (request):
    return render (request, "base2.html")


##----------------------------- BODEGGA --------------##

def consultar_bodega( request ) :
    return render ( request , "bodega/consultar_bodega.html" )


def crear_bodega( request ) :
    if request.method == "POST" :
        bodegaForm = BodegaForm ( request.POST )
        if bodegaForm.is_valid () :
            bodegaForm.save ()
            return redirect ( 'consultar_bodega' )
        else :
            bodegaForm = BodegaForm ()
    else :
        bodegaForm = BodegaForm ()
    return render ( request , "bodega/crear_bodega.html" , {'bodega' : bodegaForm} )


def eliminar_bodega( request ) :
    return render ( request , "bodega/eliminar_bodega.html" )


def modificar_bodega( request ) :
    return render ( request , "bodega/modificar_bodega.html" )


##----------------------------- BODEGA_PRODUCTO --------------##

def consultar_bodega_producto( request ) :
    return render ( request , "bodega_producto/consultar_bodega_producto.html" )


def crear_bodega_producto( request ) :
    return render ( request , "bodega_producto/crear_bodega_producto.html" )


def eliminar_bodega_producto( request ) :
    return render ( request , "bodega_producto/eliminar_bodega_producto.html" )


def modificar_bodega_producto( request ) :
    return render ( request , "bodega_producto/modificar_bodega_producto.html" )


##----------------------------- CATEGORIA_PRODUCTO --------------##

def consultar_categoria_producto( request ) :
    return render ( request , "categoria_producto/consultar_categoria_producto.html" )


def crear_categoria_producto( request ) :
    return render ( request , "categoria_producto/crear_categoria_producto.html" )


def eliminar_categoria_producto( request ) :
    return render ( request , "categoria_producto/eliminar_categoria_producto.html" )


def modificar_categoria_producto( request ) :
    return render ( request , "categoria_producto/modificar_categoria_producto.html" )


##----------------------------- DEVOLUCION --------------##

def consultar_devolucion( request ) :
    return render ( request , "devolucion/consultar_devolucion.html" )


def crear_devolucion( request ) :
    return render ( request , "devolucion/crear_devolucion.html" )


def eliminar_devolucion( request ) :
    return render ( request , "devolucion/eliminar_devolucion.html" )


def modificar_devolucion( request ) :
    return render ( request , "devolucion/modificar_devolucion.html" )


##----------------------------- EGRESO CABECERA --------------##

def consultar_egreso_cabecera( request ) :
    return render ( request , "egreso_cabecera/consultar_egreso_cabecera.html" )


def crear_egreso_cabecera( request ) :
    return render ( request , "egreso_cabecera/crear_egreso_cabecera.html" )


def eliminar_egreso_cabecera( request ) :
    return render ( request , "egreso_cabecera/eliminar_egreso_cabecera.html" )


def modificar_egreso_cabecera( request ) :
    return render ( request , "egreso_cabecera/modificar_egreso_cabecera.html" )


##----------------------------- EGRESO DETALLE --------------##

def consultar_egreso_detalle( request ) :
    return render ( request , "egreso_detalle/consultar_egreso_detalle.html" )


def crear_egreso_detalle( request ) :
    return render ( request , "egreso_detalle/crear_egreso_detalle.html" )


def eliminar_egreso_detalle( request ) :
    return render ( request , "egreso_detalle/eliminar_egreso_detalle.html" )


def modificar_egreso_detalle( request ) :
    return render ( request , "egreso_detalle/modificar_egreso_detalle.html" )


##----------------------------- INGRESO CABECERA--------------##

def consultar_ingreso_cabecera( request ) :
    return render ( request , "ingreso_cabecera/consultar_ingreso_cabecera.html" )


def crear_ingreso_cabecera( request ) :
    return render ( request , "ingreso_cabecera/crear_ingreso_cabecera.html" )


def eliminar_ingreso_cabecera( request ) :
    return render ( request , "ingreso_cabecera/eliminar_ingreso_cabecera.html" )


def modificar_ingreso_cabecera( request ) :
    return render ( request , "ingreso_cabecera/modificar_ingreso_cabecera.html" )


##----------------------------- INGRESO DETALLE--------------##

def consultar_ingreso_detalle( request ) :
    return render ( request , "ingreso_detalle/consultar_ingreso_detalle.html" )


def crear_ingreso_detalle( request ) :
    return render ( request , "ingreso_detalle/crear_ingreso_detalle.html" )


def eliminar_ingreso_detalle( request ) :
    return render ( request , "ingreso_detalle/eliminar_ingreso_detalle.html" )


def modificar_ingreso_detalle( request ) :
    return render ( request , "ingreso_detalle/modificar_ingreso_detalle.html" )


##----------------------------- PERSONA --------------##


def consultar_persona( request ) :
    persona= Persona.objects.all ()

    return render ( request , "persona/consultar_persona.html" , {'persona_ls' : persona} )


def crear_persona( request ) :
    if request.method == "POST" :
        personaForm = PersonaForm ( request.POST )
        if personaForm.is_valid () :
            personaForm.save ()
            return redirect ( 'consultar_persona' )
        else :
            personaForm = PersonaForm ()
    else :
        personaForm = PersonaForm ()

    return render ( request , "persona/crear_persona.html" , {'persona' : personaForm} )


def eliminar_persona(request, id ):
    if request.method == "POST" :
        personan = get_object_or_404(Persona, pk = id)
        personaForm = PersonaForm(request.POST or None, instance=personan)
        if personaForm.is_valid():
            personan.estado = 0
            personan.save()
            return redirect('consultar_persona')

    else :
        personan = get_object_or_404(Persona, pk = id)
        personaForm = PersonaForm(request.POST or None, instance=personan)
    return render(request,"persona/eliminar_persona.html",{'personaForm' : personaForm})


def modificar_persona( request ,id ):
    if request.method == "POST":
        personan = get_object_or_404(Persona, pk=id)
        personaForm=PersonaForm( request.POST or None,instance = personan)
        if personaForm.is_valid():
            personaForm.save()
            return redirect('consultar_persona')
        else :
            personaForm = PersonaForm (instance=personan)
    else :  ##GET
        personan = get_object_or_404(Persona, pk=id)
        personaForm = PersonaForm(request.POST or None, instance = personan)
    return render (request, "persona/modificar_persona.html" ,{'personaForm' : personaForm} )


##----------------------------- PRODUCTO --------------##

def consultar_producto( request ) :
    return render ( request , "producto/consultar_producto.html" )


def crear_producto( request ) :
    return render ( request , "producto/crear_producto.html" )


def eliminar_producto( request ) :
    return render ( request , "producto/eliminar_producto.html" )


def modificar_producto( request ) :
    return render ( request , "producto/modificar_producto.html" )


##----------------------------- PROVEEDOR --------------##

def consultar_proveedor( request ) :
    return render ( request , "proveedor/consultar_proveedor.html" )


def crear_proveedor( request ) :
    return render ( request , "proveedor/crear_proveedor.html" )


def eliminar_proveedor( request ) :
    return render ( request , "proveedor/eliminar_proveedor.html" )


def modificar_proveedor( request ) :
    return render ( request , "proveedor/modificar_proveedor.html" )


##----------------------------- ROL PERSONA--------------##


def consultar_rol_persona( request ) :
    rol_persona1 = rol_persona.objects.all ()
    return render ( request , "rol_persona/consultar_rol_persona.html", {'rol_persona1': rol_persona1} )


def crear_rol_persona( request ) :
    return render ( request , "rol_persona/crear_rol_persona.html" )


def eliminar_rol_persona( request ) :
    return render ( request , "rol_persona/eliminar_rol_persona.html" )


def modificar_rol_persona( request ) :
    return render ( request , "rol_persona/modificar_rol_persona.html" )


##----------------------------- ROL stock -------------##


def consultar_stock( request ) :
    return render ( request , "stock/consultar_stock.html" )


def crear_stock( request ) :
    return render ( request , "stock/crear_stock.html" )


def eliminar_stock( request ) :
    return render ( request , "stock/eliminar_stock.html" )


def modificar_stock( request ) :
    return render ( request , "stock/modificar_stock.html" )


##----------------------------- unidad de medida -------------##


def consultar_unidad_medida( request ) :
    return render ( request , "unidad_medida/consultar_unidad_medida.html" )


def crear_unidad_medida( request ) :
    return render ( request , "unidad_medida/crear_unidad_medida.html" )


def eliminar_unidad_medida( request ) :
    return render ( request , "unidad_medida/eliminar_unidad_medida.html" )


def modificar_unidad_medida( request ) :
    return render ( request , "unidad_medida/modificar_unidad_medida.html" )


##----------------------------- unidad de marca -------------##


def consultar_marca( request ) :
    return render ( request , "marca/consultar_marca.html" )


def crear_marca( request ) :
    return render ( request , "marca/crear_marca.html" )


def eliminar_marca( request ) :
    return render ( request , "marca/eliminar_marca.html" )


def modificar_marca( request ) :
    return render ( request , "marca/modificar_marca.html" )
