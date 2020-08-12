from django.shortcuts import render

from django.http import HttpResponse
from .models import ArticlePost

from django.shortcuts import render, redirect
from  django.http import HttpResponse

from .froms import ArticlePostForm

from django.contrib.auth.models import User

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
    context = {'article' : article}
    return render(request, 'article/detail.html', context)

def blog_create(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)

        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)

            new_article.author = User.objects.get(id=1)

            new_article.save()

            return redirect("Blog:BlogMainList")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form' : article_post_form}
        return render(request, 'article/create.html', context)