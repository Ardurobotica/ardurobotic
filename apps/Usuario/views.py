from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegistroForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('list_user')
 
 
class UserList(ListView):
    model = User
    template_name = 'Usuario/list_user.html'
