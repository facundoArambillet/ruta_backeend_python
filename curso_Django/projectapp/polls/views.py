from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    lates_question_list = Question.objects.all()  #El metodo filter trae todas las coincidencias el metodo get unicamente puede traer 1
    return render(request, "polls/index.html", {   #Render se usa para poder utilizar las views en los templates
        "lates_question_list": lates_question_list
    })

def detail(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, "polls/detail.html", {
        "question": question
    })

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando la pregunta numero {question_id}")