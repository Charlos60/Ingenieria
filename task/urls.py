from django.urls import path
from . import views

urlpatterns = [ # aqui el usario va poder acceder a lo que es la vista
    path('', views.inicio, name='inicio'),#cuando acceda a la raiz va a entrar a la vista de inicio 
    path('nosotros',views.nosotros, name='nosotros'),
    path('productos',views.productos, name='productos'),   
    path('productos/crear',views.crear, name='crear'),  
    path('productos/editar/<int:codigo_producto>/',views.editar, name='editar'),
    
    path('productos/crear/new',views.crear_producto, name='crear_producto'), 
    path('productos/borrar/<int:codigo_producto>/',views.borrar, name='borrar'), 
    path('productos/editar/update/<int:codigo_producto>/',views.editar_producto, name='editar_producto'), 
    
]