from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# Este archivo maneja la vista admin de(localhost/admin) puedo editar como se van a ver los contenidos en esa interfaz grafica de django

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3 #Define la cantidad que respuestas que me muestra por defecto en el admin


class QuestionAdmin(admin.ModelAdmin):
    fields = ["text","date"]
    inlines = [ChoiceInline]
    list_display = ("text","date","was_published_recently") #Acomodo la manera en que veo las preguntas en el admin
    list_filter = ["date"] #Se añade un filtro
    search_fields = ["text"] #Añade cuadro de busqueda

admin.site.register(Question,QuestionAdmin) #admin.site.register([Question,Choice])