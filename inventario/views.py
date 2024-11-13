from django.shortcuts import render
from .models import Producto, Categoria
from .forms import ProductoForm
from django.shortcuts import redirect

from django.db.models import Q, Count, Sum, Avg, Min, Max

# Create your views here.

def listado_productos(request):
    nombre = request.GET.get('nombre')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    fecha_vencimiento_min = request.GET.get('fecha_vencimiento_min')
    fecha_vencimiento_max = request.GET.get('fecha_vencimiento_max')
    
    contexto = {}
    productos = Producto.objects.all()
    
    if nombre:
        productos = productos.filter(nombre__icontains=nombre)
        
    if precio_min: 
        productos = productos.filter(precio__gte=precio_min)
        
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)
        
    if fecha_vencimiento_min:
        productos = productos.filter(fecha_vencimiento__gte=fecha_vencimiento_min)
         
    if fecha_vencimiento_max:
        productos = productos.filter(fecha_vencimiento__lte=fecha_vencimiento_max)
             
    contexto["productos"] = productos
    contexto["categorias"] = Categoria.objects.all()
    contexto["nombre"] = nombre
    contexto["precio_min"] = precio_min
    contexto["precio_max"] = precio_max
    contexto["fecha_vencimiento_min"] = fecha_vencimiento_min
    contexto["fecha_vencimiento_max"] = fecha_vencimiento_max
    return render(request, 'listado_productos.html', contexto)


def add_producto(request):
    
    contexto = {}
    print(request.method)
    
    if request.method == 'GET':
        contexto ["form"] = ProductoForm()
        return render(request, 'add_producto.html', contexto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_productos')
            
        return render(request, 'add_producto.html', contexto)
        
def update_producto(request):
    contexto = {}
    print(request.method)
    
    if request.method == 'GET':
        contexto ["form"] = ProductoForm()
        return render(request, 'update_producto.html', contexto)