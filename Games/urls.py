from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
        url(r"^$", "Games.views.index"),
        url(r"^game/(?P<id>\d+)$", "Games.views.gameInfo")
        )