from django.conf.urls import patterns, url

urlpatterns = patterns("",
        url(r"^add/$", "Article.views.articleAdd", name="ArticleAdd"),
        url(r"^(?P<articleID>\d+)/$", "Article.views.articleRead", name="ArticleRead"),
        )