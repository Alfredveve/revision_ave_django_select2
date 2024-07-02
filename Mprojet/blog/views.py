from django.shortcuts import render
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
    return render(request, 'blog/create.html')
