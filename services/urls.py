from django.urls import path
from . import views

urlpatterns = [
    path('', views.logueo, name="login"),
    path('singup/', views.singup, name="singup"),
    path('home/', views.home, name="home"),
    path('crudService/', views.crudServices, name="crudService"),
    path('deslogueo/', views.deslogueo, name="deslogueo"),
    path('updateservice/', views.updateservice, name="updateservice"),
    path('deleteservice/', views.deleteservice, name="deleteservice"),
]