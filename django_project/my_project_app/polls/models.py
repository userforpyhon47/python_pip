from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Published date")

    def __str__(self):
        return f"{self.question_text} {self.pub_date.__str__()}"
    
    def published_recently(self):
        current_date = timezone.now()
        return current_date >= self.pub_date >= current_date - datetime.timedelta(days=1)


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text