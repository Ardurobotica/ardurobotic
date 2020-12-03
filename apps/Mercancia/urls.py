from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import MercanciaList, MercanciaCreate, MercanciaUpdate , MercanciaDelete,MercanciaListG
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Mercancia import views


urlpatterns = [
    path('listar/', MercanciaList.as_view(), name="mercancia_list"),
    path('producto/', MercanciaListG.as_view(), name="producto_listG"),

    path('crear/', MercanciaCreate.as_view(), name="mercancia_form"),
    path('editar/<int:pk>', MercanciaUpdate.as_view(), name="mercancias_update"),
    path('borrar/<int:pk>', MercanciaDelete.as_view(), name="mercancias_borrar"),

    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
    
    
]
