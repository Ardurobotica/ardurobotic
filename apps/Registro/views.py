from django.shortcuts import render, redirect, get_object_or_404
from .models import Recomendacion
from .forms import RecomendacionesForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q 

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecomendacionSerializer

from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



# Create your views here.
def listar_recomendaciones(request):
    recomendaciones = Recomendacion.objects.all()
    return render(request, "Registro/listar_recomendaciones.html", {'recomendaciones': recomendaciones})


class RecomendacionCreate(CreateView):
    model = Recomendacion
    form_class = RecomendacionesForm
    template_name = 'Registro/recomendaciones_form.html'
    success_url = reverse_lazy('mantenedor')
    
class RecomendacionList(ListView):
    model = Recomendacion
    template_name = 'Registro/list_recomendaciones.html'
    # paginate_by = 4

class RecomendacionUpdate(UpdateView):
    model = Recomendacion
    form_class = RecomendacionesForm
    template_name = 'Registro/recomendaciones_form.html'
    success_url = reverse_lazy('list_recomendaciones')

        

class RecomendacionDelete(DeleteView):
    model = Recomendacion
    template_name = 'Registro/recomendaciones_delete.html'
    success_url = reverse_lazy('mantenedor')


def mantenedor(request):
    lista= Recomendacion.objects.all()
    nombre_producto= request.GET.get('nombre-producto')
    nombre= request.GET.get('nombre')
 
    if 'btn-nombre-producto' in request.GET:
       if nombre_producto: 
           lista= Recomendacion.objects.filter(producto__icontains=nombre_producto)
    elif 'btn-nombre' in request.GET:
        if nombre:
            lista= Recomendacion.objects.filter(nombre__icontains=nombre)
      
    data = {
        'object_list': lista
    }
    return render(request, 'Registro/list_recomendaciones_filtros.html', data)


    # El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET', 'POST'])
def recomendacion_collection(request):
    if request.method == 'GET':
        recomendaciones = Recomendacion.objects.all()
        serializer = RecomendacionSerializer(recomendaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecomendacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def recomendacion_element(request, pk):
    recomendacion = get_object_or_404(Recomendacion, id=pk)

    if request.method == 'GET':
        serializer = RecomendacionSerializer(recomendacion)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        recomendacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        recomendacion_new = JSONParser().parse(request) 
        serializer = RecomendacionSerializer(recomendacion, data=recomendacion_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
