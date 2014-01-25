# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ArticleAddForm


@login_required()
def articleAdd(request):
    """
    GET: пустая форма
    POST: добаляет в БД новую запись "article". Связывая указаные имена тагов из поля "tags" формы с записями tag в БД
    если таковые присутсвуют и добавляет в противном случае.
    """
    if request.method == "POST":
        form = ArticleAddForm(request.POST)
        if form.is_valid():
            #create new article
            title = form.cleaned_data["Title"]
            body = form.cleaned_data["Body"]
            article = Article(
                Title = title, Body = body
            )
            article.save()
            tags = form.cleaned_data["tags"].split()
            #get tags from DB and add to article
            for tagName in tags:
                tag, created = Tag.objects.get_or_create(Name = tagName)
                article.tag_set.add(tag)
            article.save()
            return HttpResponseRedirect("/")
        else:
            return render( request, "Article/articleAdd.html", {"form": form,} )
    else:
        form = ArticleAddForm()
        return render( request, "Article/articleAdd.html", {"form": form,} )


def articleRead(request, articleID):
    """
    Страница для отображения полного текста статьи

    :param articleID: ID статьи
    """
    article = get_object_or_404(Article, pk=articleID)
    return render( request, "Article/articleRead.html", {"article": article,} )