from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Game


def index(request):
    games = Game.objects.all()[:10]
    return render(request,"Games/index.html", {"user": request.user,
                                                    "games": games})

def gameInfo(request, id):
    game = Game.objects.get(id=id)
    return render(request, "Games/gameInfo.html", { "user": request.user,
                                                    "game": game})
