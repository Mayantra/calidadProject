from tempfile import template
from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.views import *

# Create your views here.
class pedidosView(TemplateView):
    template_name = 'pedidos.html'

class clientesView(TemplateView):
    template_name = 'cliente.html'

class inventarioView(TemplateView):
    template_name = 'inventario.html'

class detalleArtView(TemplateView):
    template_name = 'detalleArt.html'