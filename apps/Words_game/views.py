from django.http import HttpResponse
from django.shortcuts import render

from apps.Words_game.models import *

# Create your views here.
menu = ["home", "score", "about"]
def home_page(request):
    return render(request, "game/home.html", {"menu": menu, "Title": 'Home'})

def about_page(request):
    return render(request, "game/about.html", {"menu": menu, "Title": 'About'})

def score_page(request):
    player_score = Score.objects.all()
    context = {
        "menu": menu,
        "Title": 'Score',
        "player_score": player_score}
    return render(request, "game/score.html", context=context)