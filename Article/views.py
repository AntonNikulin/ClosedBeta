from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ArticleAddForm


@login_required()
def articleAdd(request):
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
    article = get_object_or_404(Article, pk=articleID)
    return render( request, "Article/articleRead.html", {"article": article,} )