from django.shortcuts import render

from django.http import HttpResponse
from .models import ArticlePost

def index(request):
    articles = ArticlePost.objects.all()
    context = {'articles':articles}
    return render(request, 'article/list.html', context)
