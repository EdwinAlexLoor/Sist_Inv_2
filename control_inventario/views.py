from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from .forms import PersonaForm , BodegaForm, Rol_personaForm, Categoria_productoForm, Bodega_productoForm, \
    DevolucionForm, Egreso_cabeceraForm, MarcaForm, Egreso_detalleForm, Ingreso_cabeceraForm, Ingreso_detalleForm, \
    ProductoForm, ProveedorForm, Unidad_medidaForm
from .models import Persona, rol_persona, bodega, Categoria_producto, Bodega_producto, \
    Devolucion, Egreso_cabecera, Marca, Egreso_detalle, ingreso_cabecera, ingreso_detalle, producto , \
    proveedor, unidad_medida


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


def eliminar_bodega (request,id):
    if request.method == "POST":
        bodega1 = get_object_or_404(bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega1)
        if bodegaForm.is_valid():
            bodega1.estado = 0
            bodega1.save()
            return redirect('consultar_bodega')
    else:
        bodega1 = get_object_or_404(bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega1)
    return render(request, "bodega/eliminar_bodega.html",{'bodega_ls': bodegaForm})

def modificar_bodega (request,id):
    if request.method == "POST":
        bodega1 = get_object_or_404(bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega1)
        if bodegaForm.is_valid():
            bodegaForm.save()
            return redirect('consultar_bodega')
        else:
            bodegaForm = BodegaForm(instance=bodega1)
    else:  ##GET
        bodega1 = get_object_or_404(bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega1)
    return render(request, "bodega/modificar_bodega.html",{'bodega_ls': bodegaForm})


##----------------------------- BODEGA_PRODUCTO --------------##

def consultar_bodega_producto (request):
    bodega_producto1 = bodega.objects.all()
    return render(request, "bodega_producto/consultar_bodega_producto.html",{'bodega_producto_ls': bodega_producto1})

def crear_bodega_producto (request):
    if request.method == "POST":
        bodega_productoForm = Bodega_productoForm(request.POST)
        if bodega_productoForm.is_valid():
            bodega_productoForm.save()
            return redirect('consultar_bodega_producto')
        else:
            bodega_productoForm = Bodega_productoForm()
    else:
         bodega_productoForm = Bodega_productoForm ()
    return render(request, "bodega_producto/crear_bodega_producto.html",{'bodega_producto_ls': bodega_productoForm})

def eliminar_bodega_producto (request,id):
    if request.method == "POST":
        bodega_producto1 = get_object_or_404(Bodega_producto, pk=id)
        bodega_productoForm = Bodega_productoForm(request.POST or None, instance=bodega_producto1)
        if bodega_productoForm.is_valid():
            bodega_producto1.estado = 0
            bodega_producto1.save()
            return redirect('consultar_bodega_producto')
    else:
        bodega_producto1 = get_object_or_404(Bodega_producto, pk=id)
        bodega_productoForm = BodegaForm(request.POST or None, instance=bodega_producto1)
    return render(request, "bodega_producto/eliminar_bodega_producto.html",{'bodega_producto_ls': bodega_productoForm})

def modificar_bodega_producto (request,id):
    if request.method == "POST":
        bodega_producto1 = get_object_or_404(Bodega_producto, pk=id)
        bodega_productoForm = Bodega_productoForm(request.POST or None, instance=bodega_producto1)
        if bodega_productoForm.is_valid():
            bodega_productoForm.save()
            return redirect('consultar_bodega_producto')
        else:
            bodega_productoForm = Bodega_productoForm(instance=bodega_producto1)
    else:  ##GET
        bodega_producto1 = get_object_or_404(Bodega_producto, pk=id)
        bodega_productoForm = Bodega_productoForm(request.POST or None, instance=bodega_producto1)
    return render(request, "bodega_producto/modificar_bodega_producto.html",{'bodega_producto_ls': bodega_productoForm})


##----------------------------- CATEGORIA_PRODUCTO --------------##

def consultar_categoria_producto (request):
    categoria_producto1 = Categoria_producto.objects.all()
    return render(request, "categoria_producto/consultar_categoria_producto.html",{'categoria_producto_ls': categoria_producto1})

def crear_categoria_producto (request):
    if request.method == "POST":
        categoria_productoForm = Categoria_productoForm(request.POST)
        if categoria_productoForm.is_valid():
            categoria_productoForm.save()
            return redirect('consultar_categoria_producto')
        else:
           categoria_productoForm = Categoria_productoForm()
    else:
         categoria_productoForm = Categoria_productoForm ()
    return render(request, "categoria_producto/crear_categoria_producto.html",{'categoria_producto_ls': categoria_productoForm})

def eliminar_categoria_producto (request,id):
    if request.method == "POST":
        categoria_producto1 = get_object_or_404(Categoria_producto, pk=id)
        categoria_productoForm = Categoria_productoForm(request.POST or None, instance=categoria_producto1)
        if categoria_productoForm.is_valid():
            categoria_producto1.estado = 0
            categoria_producto1.save()
            return redirect('consultar_categoria_producto')
    else:
        categoria_producto1 = get_object_or_404(Categoria_producto, pk=id)
        categoria_productoForm = Categoria_productoForm(request.POST or None, instance=categoria_producto1)
    return render(request, "categoria_producto/eliminar_categoria_producto.html",{'categoria_producto_ls': categoria_productoForm})

def modificar_categoria_producto (request,id):
    if request.method == "POST":
        categoria_producto1 = get_object_or_404(Categoria_producto, pk=id)
        categoria_productoForm = Categoria_productoForm(request.POST or None, instance=categoria_producto1)
        if categoria_productoForm.is_valid():
            categoria_productoForm.save()
            return redirect('consultar_categoria_producto')
        else:
            categoria_productoForm = Categoria_productoForm(instance=categoria_producto1)
    else:  ##GET
        categoria_producto1 = get_object_or_404(Categoria_producto, pk=id)
        categoria_productoForm = Categoria_productoForm(request.POST or None, instance=categoria_producto1)
    return render(request, "categoria_producto/modificar_categoria_producto.html",{'categoria_producto_ls': categoria_productoForm})


##----------------------------- DEVOLUCION --------------##

def consultar_devolucion(request):
    devolucion1 = Devolucion.objects.all()
    return render(request, "devolucion/consultar_devolucion.html",{'devolucion_ls': devolucion1})

def crear_devolucion(request):
    if request.method == "POST":
        devolucionForm = DevolucionForm(request.POST)
        if devolucionForm.is_valid():
            devolucionForm.save()
            return redirect('consultar_devolucion')
        else:
           devolucionForm = DevolucionForm()
    else:
         devolucionForm = DevolucionForm ()
    return render(request, "devolucion/crear_devolucion.html",{'devolucion_ls': devolucionForm})

def eliminar_devolucion(request,id):
    if request.method == "POST":
        devolucion1 = get_object_or_404(Devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion1)
        if devolucionForm.is_valid():
            devolucion1.estado = 0
            devolucion1.save()
            return redirect('consultar_devolucion')
    else:
        devolucion1 = get_object_or_404(Devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion1)
    return render(request, "devolucion/eliminar_devolucion.html",{'devolucion_ls': devolucionForm})

def modificar_devolucion(request,id):
    if request.method == "POST":
        devolucion1 = get_object_or_404(Devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion1)
        if devolucionForm.is_valid():
            devolucionForm.save()
            return redirect('consultar_devolucion')
        else:
            devolucionForm = DevolucionForm(instance=devolucion1)
    else:  ##GET
        devolucion1 = get_object_or_404(Devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion1)
    return render(request, "devolucion/modificar_devolucion.html",{'devolucion_ls': devolucionForm})


##----------------------------- EGRESO CABECERA --------------##

def consultar_egreso_cabecera (request):
    egreso_cabecera1 = Egreso_cabecera.objects.all()
    return render(request, "egreso_cabecera/consultar_egreso_cabecera.html",{'egreso_cabecera_ls': egreso_cabecera1})

def crear_egreso_cabecera (request):
    if request.method == "POST":
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST)
        if egreso_cabeceraForm.is_valid():
            egreso_cabeceraForm.save()
            return redirect('consultar_egreso_cabecera')
        else:
            egreso_cabeceraForm = Egreso_cabeceraForm()
    else:
         egreso_cabeceraForm = Egreso_cabeceraForm ()
    return render(request, "egreso_cabecera/crear_egreso_cabecera.html",{'egreso_cabecera_ls': egreso_cabeceraForm})

def eliminar_egreso_cabecera (request,id):
    if request.method == "POST":
        egreso_cabecera1 = get_object_or_404(Egreso_cabecera, pk=id)
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST or None, instance=egreso_cabecera1)
        if egreso_cabeceraForm.is_valid():
            egreso_cabecera1.estado = 0
            egreso_cabecera1.save()
            return redirect('consultar_egreso_cabecera')
    else:
        egreso_cabecera1 = get_object_or_404(Egreso_cabecera, pk=id)
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST or None, instance=egreso_cabecera1)
    return render(request, "egreso_cabecera/eliminar_egreso_cabecera.html",{'egreso_cabecera_ls':egreso_cabeceraForm})

def modificar_egreso_cabecera (request,id):
    if request.method == "POST":
        egreso_cabecera1 = get_object_or_404(Egreso_cabecera, pk=id)
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST or None, instance=egreso_cabecera1)
        if egreso_cabeceraForm.is_valid():
            egreso_cabeceraForm.save()
            return redirect('consultar_egreso_cabecera')
        else:
            egreso_cabeceraForm = Egreso_cabeceraForm(instance=egreso_cabecera1)
    else:  ##GET
        egreso_cabecera1 = get_object_or_404(Egreso_cabecera, pk=id)
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST or None, instance=egreso_cabecera1)
    return render(request, "egreso_cabecera/modificar_egreso_cabecera.html",{'egreso_cabecera_ls':egreso_cabeceraForm})


##----------------------------- EGRESO DETALLE --------------##

def consultar_egreso_detalle (request):
    egreso_detalle1 = Egreso_detalle.objects.all()
    return render(request, "egreso_detalle/consultar_egreso_detalle.html",{'egreso_detalle_ls': egreso_detalle1})

def crear_egreso_detalle (request):
    if request.method == "POST":
        egreso_detalleForm = Egreso_detalleForm(request.POST)
        if egreso_detalleForm.is_valid():
            egreso_detalleForm.save()
            return redirect('consultar_egreso_detalle')
        else:
          egreso_detalleForm = Egreso_detalleForm()
    else:
         egreso_detalleForm = Egreso_detalleForm ()
    return render(request, "egreso_detalle/crear_egreso_detalle.html",{'egreso_detalle_ls': egreso_detalleForm})

def eliminar_egreso_detalle (request,id):
    if request.method == "POST":
        egreso_detalle1 = get_object_or_404(Egreso_detalle, pk=id)
        egreso_detalleForm = Egreso_detalleForm(request.POST or None, instance=egreso_detalle1)
        if egreso_detalleForm.is_valid():
            egreso_detalle1.estado = 0
            egreso_detalle1.save()
            return redirect('consultar_egreso_detalle')
    else:
        egreso_detalle1 = get_object_or_404(Egreso_detalle, pk=id)
        egreso_detalleForm = Egreso_detalleForm(request.POST or None, instance=egreso_detalle1)
    return render(request, "egreso_detalle/eliminar_egreso_detalle.html",{'egreso_detalle_ls': egreso_detalleForm})

def modificar_egreso_detalle (request,id):
    if request.method == "POST":
        egreso_detalle1 = get_object_or_404(Egreso_detalle, pk=id)
        egreso_detalleForm = Egreso_detalleForm(request.POST or None, instance=egreso_detalle1)
        if egreso_detalleForm.is_valid():
            egreso_detalleForm.save()
            return redirect('consultar_egreso_detalle')
        else:
            egreso_detalleForm = Egreso_detalleForm(instance=egreso_detalle1)
    else:  ##GET
        egreso_detalle1 = get_object_or_404(Egreso_detalle, pk=id)
        egreso_detalleForm = Egreso_detalleForm(request.POST or None, instance=egreso_detalle1)
    return render(request, "egreso_detalle/modificar_egreso_detalle.html",{'egreso_detalle_ls':egreso_detalleForm})


##----------------------------- INGRESO CABECERA--------------##

def consultar_ingreso_cabecera (request):
    ingreso_cabecera1 = ingreso_cabecera.objects.all()
    return render(request, "ingreso_cabecera/consultar_ingreso_cabecera.html",{'ingreso_cabecera': ingreso_cabecera1})

def crear_ingreso_cabecera (request):
    if request.method == "POST":
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST)
        if ingreso_cabeceraForm.is_valid():
            ingreso_cabeceraForm.save()
            return redirect('consultar_ingreso_cabecera')
        else:
          ingreso_cabeceraForm = Ingreso_cabeceraForm()
    else:
         ingreso_cabeceraForm = Ingreso_cabeceraForm ()
    return render(request, "ingreso_cabecera/crear_ingreso_cabecera.html",{'ingreso_cabecera': ingreso_cabeceraForm})

def eliminar_ingreso_cabecera (request,id):
    if request.method == "POST":
        ingreso_cabecera1 = get_object_or_404(ingreso_cabecera, pk=id)
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST or None, instance=ingreso_cabecera1)
        if ingreso_cabeceraForm.is_valid():
            ingreso_cabecera1.estado = 0
            ingreso_cabecera1.save()
            return redirect('consultar_ingreso_cabecera')
    else:
        ingreso_cabecera1 = get_object_or_404(ingreso_cabecera, pk=id)
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST or None, instance=ingreso_cabecera1)
    return render(request, "ingreso_cabecera/eliminar_ingreso_cabecera.html",{'ingreso_cabecera': ingreso_cabeceraForm})

def modificar_ingreso_cabecera (request,id):
    if request.method == "POST":
        ingreso_cabecera1 = get_object_or_404(ingreso_cabecera, pk=id)
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST or None, instance=ingreso_cabecera1)
        if ingreso_cabeceraForm.is_valid():
            ingreso_cabeceraForm.save()
            return redirect('consultar_ingreso_cabecera')
        else:
            ingreso_cabeceraForm = Ingreso_cabeceraForm(instance=ingreso_cabecera1)
    else:  ##GET
        ingreso_cabecera1 = get_object_or_404(ingreso_cabecera, pk=id)
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST or None, instance=ingreso_cabecera1)
    return render(request, "ingreso_cabecera/modificar_ingreso_cabecera.html",{'ingreso_cabecera': ingreso_cabeceraForm})


##----------------------------- INGRESO DETALLE--------------##

def  consultar_ingreso_detalle (request):
    ingreso_detalle1 = ingreso_detalle.objects.all()
    return render(request, "ingreso_detalle/consultar_ingreso_detalle.html",{'ingreso_detalle_ls':ingreso_detalle1})

def crear_ingreso_detalle (request):
    if request.method == "POST":
        ingreso_detalleForm = Ingreso_detalleForm(request.POST)
        if ingreso_detalleForm.is_valid():
            ingreso_detalleForm.save()
            return redirect('consultar_ingreso_detalle')
        else:
            ingreso_detalleForm = Ingreso_detalleForm()
    else:
         ingreso_detalleForm = Ingreso_detalleForm ()
    return render(request, "ingreso_detalle/crear_ingreso_detalle.html",{'ingreso_detalle_ls':ingreso_detalleForm})

def eliminar_ingreso_detalle (request,id):
    if request.method == "POST":
        ingreso_detalle1 = get_object_or_404(ingreso_detalle, pk=id)
        ingreso_detalleForm = Ingreso_detalleForm(request.POST or None, instance=ingreso_detalle1)
        if ingreso_detalleForm.is_valid():
            ingreso_detalle1.estado = 0
            ingreso_detalle1.save()
            return redirect('consultar_ingreso_detalle')
    else:
        ingreso_detalle1 = get_object_or_404(ingreso_detalle, pk=id)
        ingreso_detalleForm = Ingreso_detalleForm(request.POST or None, instance=ingreso_detalle1)
    return render(request, "ingreso_detalle/eliminar_ingreso_detalle.html",{'ingreso_detalle_ls':ingreso_detalleForm})

def modificar_ingreso_detalle (request,id):
    if request.method == "POST":
        ingreso_detalle1 = get_object_or_404(ingreso_detalle, pk=id)
        ingreso_detalleForm = Ingreso_detalleForm(request.POST or None, instance=ingreso_detalle1)
        if ingreso_detalleForm.is_valid():
            ingreso_detalleForm.save()
            return redirect('consultar_ingreso_detalle')
        else:
            ingreso_detalleForm = Ingreso_detalleForm(instance=ingreso_detalle1)
    else:  ##GET
        ingreso_detalle1 = get_object_or_404(ingreso_detalle, pk=id)
        ingreso_detalleForm = Ingreso_detalleForm(request.POST or None, instance=ingreso_detalle1)
    return render(request, "ingreso_detalle/modificar_ingreso_detalle.html",{'ingreso_detalle_ls':ingreso_detalleForm})


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

def consultar_producto(request):
    producto1 = producto.objects.all()
    return render(request, "producto/consultar_producto.html",{'producto_ls': producto1})

def crear_producto(request):
    if request.method == "POST":
        productoForm = ProductoForm(request.POST)
        if productoForm.is_valid():
            productoForm.save()
            return redirect('consultar_producto')
        else:
            productoForm = ProductoForm()
    else:
         productoForm = ProductoForm ()
    return render(request, "producto/crear_producto.html",{'producto_ls': productoForm})

def eliminar_producto(request,id):
    if request.method == "POST":
        producto1 = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto1)
        if productoForm.is_valid():
            producto1.estado = 0
            producto1.save()
            return redirect('consultar_producto')
    else:
        producto1 = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto1)
    return render(request, "producto/eliminar_producto.html",{'producto_ls': productoForm})

def modificar_producto(request,id):
    if request.method == "POST":
        producto1 = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto1)
        if productoForm.is_valid():
            productoForm.save()
            return redirect('consultar_producto')
        else:
            productoForm = ProductoForm(instance=producto1)
    else:  ##GET
        producto1 = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto1)
    return render(request, "producto/modificar_producto.html",{'producto_ls': productoForm})


##----------------------------- PROVEEDOR --------------##

def consultar_proveedor(request):
    proveedor1 = proveedor.objects.all()
    return render(request, "proveedor/consultar_proveedor.html",{'proveedor_ls': proveedor1})

def crear_proveedor(request):
    if request.method == "POST":
        proveedorForm = ProveedorForm(request.POST)
        if proveedorForm.is_valid():
            proveedorForm.save()
            return redirect('consultar_proveedor')
        else:
            proveedorForm = ProveedorForm()
    else:
         proveedorForm = ProveedorForm ()
    return render(request, "proveedor/crear_proveedor.html",{'proveedor_ls': proveedorForm})

def eliminar_proveedor(request,id):
    if request.method == "POST":
        proveedor1 = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedor1)
        if proveedorForm.is_valid():
            proveedor1.estado = 0
            proveedor1.save()
            return redirect('consultar_proveedor')
    else:
        proveedor1 = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedor1)
    return render(request, "proveedor/eliminar_proveedor.html",{'proveedor_ls': proveedorForm})

def modificar_proveedor(request,id):
    if request.method == "POST":
        proveedor1 = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedor1)
        if proveedorForm.is_valid():
            proveedorForm.save()
            return redirect('consultar_proveedor')
        else:
            proveedorForm = ProveedorForm(instance=proveedor1)
    else:  ##GET
        proveedor1 = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedor1)
    return render(request, "proveedor/modificar_proveedor.html",{'proveedor_ls': proveedorForm})


##----------------------------- ROL PERSONA--------------##


def consultar_rol_persona (request):
    rol_persona1 = bodega.objects.all()
    return render(request, "rol_persona/consultar_rol_persona.html",{'rol_persona_ls': rol_persona1})

def crear_rol_persona (request):
    if request.method == "POST":
        rol_personaForm = Rol_personaForm(request.POST)
        if rol_personaForm.is_valid():
            rol_personaForm.save()
            return redirect('consultar_rol_persona')
        else:
            rol_personaForm = Rol_personaForm()
    else:
         rol_personaForm = Rol_personaForm ()
    return render(request, "rol_persona/crear_rol_persona.html",{'rol_persona_ls': rol_personaForm})

def eliminar_rol_persona (request,id):
    if request.method == "POST":
        rol_persona1 = get_object_or_404(rol_persona, pk=id)
        rol_personaForm = Rol_personaForm(request.POST or None, instance=rol_persona1)
        if rol_personaForm.is_valid():
            rol_persona1.estado = 0
            rol_persona1.save()
            return redirect('consultar_rol_persona')
    else:
        rol_persona1 = get_object_or_404(rol_persona, pk=id)
        rol_personaForm = Rol_personaForm(request.POST or None, instance=rol_persona1)
    return render(request, "rol_persona/eliminar_rol_persona.html",{'rol_persona_ls': rol_personaForm})

def modificar_rol_persona (request,id):
    if request.method == "POST":
        rol_persona1 = get_object_or_404(rol_persona, pk=id)
        rol_personaForm = Rol_personaForm(request.POST or None, instance=rol_persona1)
        if rol_personaForm.is_valid():
            rol_personaForm.save()
            return redirect('consultar_rol_persona')
        else:
            rol_personaForm = Rol_personaForm(instance=rol_persona1)
    else:  ##GET
        rol_persona1 = get_object_or_404(rol_persona, pk=id)
        rol_personaForm = Rol_personaForm(request.POST or None, instance=rol_persona1)
    return render(request, "rol_persona/modificar_rol_persona.html",{'rol_persona_ls': rol_personaForm})


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


def consultar_unidad_medida (request):
    unidad_medida1 = unidad_medida.objects.all()
    return render(request, "unidad_medida/consultar_unidad_medida.html",{'unidad_media_ls':unidad_medida1})

def crear_unidad_medida (request):
    if request.method == "POST":
        unidad_medidaForm = Unidad_medidaForm(request.POST)
        if unidad_medidaForm.is_valid():
            unidad_medidaForm.save()
            return redirect('consultar_unidad_medida')
        else:
            unidad_medidaForm = Unidad_medidaForm()
    else:
         unidad_medidaForm = Unidad_medidaForm ()
    return render(request, "unidad_medida/crear_unidad_medida.html",{'unidad_medida_ls':unidad_medidaForm})

def eliminar_unidad_medida(request,id):
    if request.method == "POST":
        unidad_medida1 = get_object_or_404(unidad_medida, pk=id)
        unidad_medidaForm = Unidad_medidaForm(request.POST or None, instance=unidad_medida1)
        if unidad_medidaForm.is_valid():
            unidad_medida1.estado = 0
            unidad_medida1.save()
            return redirect('consultar_unidad_medida')
    else:
        unidad_medida1 = get_object_or_404(unidad_medida, pk=id)
        unidad_medidaForm = Unidad_medidaForm(request.POST or None, instance=unidad_medida1)
    return render(request, "unidad_medida/eliminar_unidad_medida.html",{'unidad_medida_ls':unidad_medidaForm})

def modificar_unidad_medida (request,id):
    if request.method == "POST":
        unidad_medida1 = get_object_or_404(unidad_medida, pk=id)
        unidad_medidaForm = Unidad_medidaForm(request.POST or None, instance=unidad_medida1)
        if unidad_medidaForm.is_valid():
            unidad_medidaForm.save()
            return redirect('consultar_unidad_medida')
        else:
            unidad_medidaForm = Unidad_medidaForm(instance=unidad_medida)
    else:  ##GET
        unidad_medida1 = get_object_or_404(unidad_medida, pk=id)
        unidad_medidaForm = Unidad_medidaForm(request.POST or None, instance=unidad_medida1)
    return render(request, "unidad_medida/modificar_unidad_medida.html",{'unidad_medida_ls':unidad_medidaForm})


##----------------------------- unidad de marca -------------##


def  consultar_marca(request):
    marca1 = Marca.objects.all()
    return render(request, "marca/consultar_marca.html",{'marca_ls': marca1})

def crear_marca (request):
    if request.method == "POST":
        marcaForm = MarcaForm(request.POST)
        if marcaForm.is_valid():
            marcaForm.save()
            return redirect('consultar_marca')
        else:
            marcaForm = MarcaForm()
    else:
         marcaForm = MarcaForm ()
    return render(request, "marca/crear_marca.html",{'marca_ls': marcaForm})

def eliminar_marca (request,id):
    if request.method == "POST":
        marca1 = get_object_or_404(Marca, pk=id)
        marcaForm = MarcaForm(request.POST or None, instance=marca1)
        if marcaForm.is_valid():
            marca1.estado = 0
            marca1.save()
            return redirect('consultar_marca')
    else:
        marca1 = get_object_or_404(Marca, pk=id)
        marcaForm = MarcaForm(request.POST or None, instance=marca1)
    return render(request, "marca/eliminar_marca.html",{'marca_ls': marcaForm})

def modificar_marca (request,id):
    if request.method == "POST":
        marca1 = get_object_or_404(Marca, pk=id)
        marcaForm = MarcaForm(request.POST or None, instance=marca1)
        if marcaForm.is_valid():
            marcaForm.save()
            return redirect('consultar_marca')
        else:
            marcaForm = MarcaForm(instance=marca1)
    else:  ##GET
        marca1 = get_object_or_404(Marca, pk=id)
        marcaForm = MarcaForm(request.POST or None, instance=marca1)
    return render(request, "marca/modificar_marca.html",{'marca_ls': marcaForm})
