from django.urls import path
from . import views

urlpatterns = [
    path('autor/', views.cadastrar_autor, name='cadastrar_autor'),
    path('post/', views.cadastrar_post, name='cadastrar_post'),
    path('comentario/', views.cadastrar_comentario, name='cadastrar_comentario'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
