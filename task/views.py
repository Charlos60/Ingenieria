from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse 
from .models import Task



# Create your views here.

def inicio(request): #funcion que recibe un request y responde con una pagina en este caso 
    
    return render(request,'paginas/inicio.html')


def nosotros(request): #funcion que rec
    return render(request,'paginas/nosotros.html')
def productos(request):
    task=Task.objects.all()
    return render(request,'vistasProductos/index.html',{'task':task})
def crear(request):
    return render(request,'vistasProductos/crear.html')
    
def editar(request,codigo_producto):
    task=Task.objects.get(codigo=codigo_producto)
    return render(request,'vistasProductos/editar.html',{'task':task})
    """return render(request,'vistasProductos/editar.html',{'task':task})"""

def crear_producto(request):
    task= Task(codigo=request.POST['codigo'],descripcion=request.POST['descripcion'],precio=request.POST['precio'],cantidad=request.POST['cantidad'],categoria=request.POST['categoria'],descripcion_categoria=request.POST['descripcion_categoria'])
    task.save()
    print(request.POST)
    return redirect('/productos')

def borrar(request,codigo_producto):
    print(codigo_producto)
    task= Task.objects.get(codigo=codigo_producto)
    task.delete()
    return redirect('/productos') 
def editar_producto(request,codigo_producto):
    codigo=codigo_producto
    descripcion=request.POST['descripcion']
    precio=request.POST['precio']
    cantidad=request.POST['cantidad']
    categoria=request.POST['categoria']
    descripcion_categoria=request.POST['descripcion_categoria']

    task=Task.objects.get(codigo=codigo_producto)
    task.codigo=codigo
    task.descripcion=descripcion
    task.precio=precio
    task.cantidad=cantidad
    task.categoria=categoria
    task.descripcion_categoria=descripcion_categoria
    task.save()
    return redirect('/productos')
