from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Question, Choice
from django.views.generic import ListView, DetailView
from django.utils import timezone


class IndexView(ListView):
    model = Question
    template_name = "polls/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        current_time = timezone.now()
        return Question.objects.filter(pub_date__lte=current_time).order_by("-pub_date")[:5]

# def index(request):
#     question_list = Question.objects.all()
#     context = {"question_list": question_list}
#     return render(request=request,template_name="polls/index.html",context=context)

class DetailsView(DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.filter(pub_date__lte=timezone.now())

# def detail(request, question_id):
#     try:
#         #question = get_object_or_404(klass=Question, pk=question_id)
#         question = Question.objects.get(pk=question_id)
#         context = {"question": question}
#     except Question.DoesNotExist:
#            return render(request=request, template_name="polls/404.html")
#     return render(request=request, template_name="polls/detail.html", context=context)

class ResultView(DetailView):
    model = Question
    template_name = "polls/result.html"

# def result(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         return render(request=request, template_name="polls/404.html")
#     else:
#         return render(request=request, template_name="polls/result.html", 
#                       context={"question":question})
    

def vote(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
        question_choice = question.choice_set.get(pk=request.POST["choice"])
        question_choice.votes += 1
        question_choice.save()
    except (KeyError, Choice.DoesNotExist):
        return render(request=request, template_name="polls/detail.html", 
                      context={"question":question,
                               "error": "Select a valid option first"})
    return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))

