from django.shortcuts import render, redirect
from .forms import AutorForm, PostForm, ComentarioForm
from .models import Post

def cadastrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_autor')
    else:
        form = AutorForm()
    return render(request, 'blog/form_autor.html', {'form': form})

def cadastrar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_post')
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form})

def cadastrar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_comentario')
    else:
        form = ComentarioForm()
    return render(request, 'blog/form_comentario.html', {'form': form})

def buscar_post(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'blog/buscar.html', {'resultados': resultados, 'query': query})

