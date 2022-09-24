from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.views import *

# Create your views here.
class baseView (TemplateView):
    template_name = 'base.html'

class base2View(TemplateView):
    template_name = "base2.html"

class base3View(TemplateView):
    template_name = "base3.html"

class inicioView (TemplateView):
    template_name = 'index.html'

class nuevoView(TemplateView):
    template_name = 'loNuevo.html'

class loginXView(LoginView):
    template_name = 'registro/login.html'

class proOficinaView(TemplateView):
    template_name = 'proOficina.html'

class carritoView(TemplateView):
    template_name = 'carrito.html'

    


