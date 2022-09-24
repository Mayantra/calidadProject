from xmlrpc import client
from django.contrib import admin
from django.urls import path 
from .views import *

app_name = 'front'
urlpatterns =[
    path('index/',inicioView.as_view(), name='index'),
    path('base/', baseView.as_view(), name = 'base'),
    path('base2/', base2View.as_view(), name= 'base2'),
    path('base3/', base3View.as_view(), name='base3'),
    path('login/', loginXView.as_view(), name='login'),
    path('loNuevo/', nuevoView.as_view(), name='loNuevo'),
    path('proOficina/', proOficinaView.as_view(), name='proOficina'),
    path('carrito/', carritoView.as_view(), name='carrito'),
    
]