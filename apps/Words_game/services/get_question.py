import random

from apps.Words_game.models import Word


def get_question():
    return get_question_by_id(random.randint(1, 5))


def get_question_by_id(uid):
    return Word.objects.get(id=uid)

