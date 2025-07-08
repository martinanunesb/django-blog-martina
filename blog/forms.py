from django import forms
from .models import Autor, Post, Comentario

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email', 'bio']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'autor']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'email', 'conteudo', 'post']
