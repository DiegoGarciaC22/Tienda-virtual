from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Producto, Categoria

""" VISTAS PARA EL CATALOGO DE PRODUCTOS """

def index(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()
    context = {
        'productos':listaProductos,
        'categorias':listaCategorias,
    }
    return render(request, 'index.html', context)

def productosPorCategoria(request, categoria_id):
    """ vista para filtrar por categoria """
    
    objCategoria = get_object_or_404(Categoria, pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()
    listaCategoria = Categoria.objects.all()
    context = {
        'productos':listaProductos,
        'categorias':listaCategoria
    }
    return render(request, 'index.html', context)


def productosPorNombre(request):
    """ vista para filtrado de productos por nombre """
    
    nombre = request.POST['nombre']
    listaProductos = Producto.objects.filter(nombre__icontains=nombre)
    listaCategorias = Categoria.objects.all()
    context = { 
        'categorias':listaCategorias,
        'productos':listaProductos
    }
    return render(request,'index.html',context)    
    

def productoDetalle(request, producto_id):
    """ vista del detalle del producto """    
    objProducto = get_object_or_404(Producto, pk=producto_id)
    context = {
        'producto': objProducto
    }
    return render(request, 'producto.html', context)
    

