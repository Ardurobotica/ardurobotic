from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [

    # listar las recomendaciones de la bd
    path('listarRecomendaciones', views.listar_recomendaciones, name="listar_recomendaciones"),
    

    # llamando a la clases 
    path('add_recomendacion', views.RecomendacionCreate.as_view(), name="add_recomendacion"),

    path('list_recomendaciones/', views.RecomendacionList.as_view(), name='list_recomendaciones'),


    path('edit_recomendacion/<int:pk>', login_required(views.RecomendacionUpdate.as_view()), name='edit_recomendacion'),

    path('del_recomendacion/<int:pk>', login_required(views.RecomendacionDelete.as_view()), name='del_recomendacion'),

    path('mantenedor/', views.mantenedor , name="mantenedor"), 

    path('recomendaciones/',  views.recomendacion_collection , name='recomendacion_collection'),
    path('recomendaciones/<int:pk>/', views.recomendacion_element ,name='recomendacion_element')

]