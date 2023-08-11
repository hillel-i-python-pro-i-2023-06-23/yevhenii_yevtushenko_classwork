from django.db import models


# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(max_length=50)
    question = models.CharField(max_length=50)



class Answer(models.Model):
    answer = models.TextField(max_length=100)
    qid = models.IntegerField()

