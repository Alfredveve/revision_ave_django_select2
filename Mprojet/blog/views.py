from django.shortcuts import render, redirect
from .models import BlogArticles
from .forms import BlogArticlesForm


def index(request):
    blog = BlogArticles.objects.all()

    context = {
        'blogs': blog
    }
    return render(request, 'blog/index.html', context)


def addBlog(request):
    form = BlogArticlesForm(request.POST or None, request.FILES or None)
    messages = ""
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = BlogArticlesForm()
        messages = "We have receive successfully an item"
    return render(request, 'blog/create.html', {'form': form, 'message': messages})

def listblog(request):
    blog = BlogArticles.objects.all()
    context = {
        'blogs' : blog
    }
    return render(request, 'blog/table.html', context)


def modifierblog(request, pk):
    obj = BlogArticles.objects.get(id=pk)
    form = BlogArticlesForm(request.POST or None, request.FILES or None, instance = obj)
    messages = ""
    if request.method == "POST" and form.is_valid():
        form.save()
        form = BlogArticles()
        messages = "We have modified successfully"
    return render(request, 'blog/modifier.html', {'form': form, 'message': messages})
