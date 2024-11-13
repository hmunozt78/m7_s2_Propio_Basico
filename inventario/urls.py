from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listado_productos,name='listado_productos'),
    path('add/', views.add_producto,name='add_productos'),
    path('update/', views.update_producto,name='update_productos'),
]
