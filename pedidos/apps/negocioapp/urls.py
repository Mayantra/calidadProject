from xmlrpc import client
from django.contrib import admin
from django.urls import path 
from .views import *

app_name = 'negocio'
urlpatterns =[
    path('cliente/', clientesView.as_view(), name='clientes'),
    path('pedidos/', pedidosView.as_view(), name='pedidos'),
    path('inventario/', inventarioView.as_view(), name='inventario'),
    path('detalleArt/', detalleArtView.as_view(), name='detalleArt'),
]