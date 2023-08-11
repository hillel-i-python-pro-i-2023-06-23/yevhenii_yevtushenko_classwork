from django.http import HttpResponse
from django.shortcuts import render

from apps.Words_game.forms import AnswerForm
from apps.Words_game.models import *
from apps.Words_game.services.answer_validator import answer_validator
from apps.Words_game.services.get_question import get_question

# Create your views here.
menu = ["home", "score", "about", "game"]
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


def game_page(request):
    question = ""

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            if answer_validator(form.qid, form.answer):
                return HttpResponse("Correct Answer")
            else:
                return HttpResponse("Wrong Answer")

    else:
        form = AnswerForm()
        word = get_question()
        form.qid = word.id
        question = word.question

    return render(request, "game/game.html", {"menu": menu, "Title": 'Game', "form": form, "question": question })