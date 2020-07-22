from django.shortcuts import render

from django.http import HttpResponse
from .models import ArticlePost

import sys
import markdown

def blog_main_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles':articles}
    return render(request, 'article/list.html', context)

def blog_detail(request, id):
    article = ArticlePost.objects.get(id=id)

    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    print(article.body)
    context = {'article':article}
    return render(request, 'article/detail.html', context)