import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    # id este atributo ya Django lo crea automaticamente por lo que no hay que ponerlo
    text = models.CharField(max_length= 200)
    date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.text

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # id este atributo ya Django lo crea automaticamente por lo que no hay que ponerlo
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length= 200)
    votes = models.IntegerField(default= 0)

    def __str__(self) -> str:
        return self.text
 