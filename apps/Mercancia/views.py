from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import MercanciaSerializer


from .models import Mercancia
from .forms import MercanciaForm
# Create your views here.

class MercanciaList (ListView):                    
    model = Mercancia
    template_name = 'Mercancia/mercancia_list.html'

class MercanciaListG (ListView):                    
    model = Mercancia
    template_name = 'Mercancia/productos.html'

class MercanciaCreate(CreateView):
    model = Mercancia
    form_class = MercanciaForm
    template_name = 'Mercancia/mercancia_form.html'
    success_url = reverse_lazy('mercancia_list')

class MercanciaUpdate(UpdateView):
    model = Mercancia
    form_class = MercanciaForm
    template_name = 'Mercancia/mercancia_form.html'
    success_url = reverse_lazy('mercancia_list')

class MercanciaDelete(DeleteView):
    model = Mercancia
    template_name = 'Mercancia/mercancia_borrar.html'
    success_url = reverse_lazy('mercancia_list')



# ----- Clases para la API----------

class API_objects(generics.ListCreateAPIView):
    queryset = Mercancia.objects.all()
    serializer_class = MercanciaSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mercancia.objects.all()
    serializer_class = MercanciaSerializer
