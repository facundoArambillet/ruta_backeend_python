import datetime

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone
from .models import Question
# Create your tests here.


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(
            text="Que curso es el mejor aplicado?", date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns False for questions whose date is in the past"""
        time = timezone.now() - datetime.timedelta(days=1, hours=1)
        past_question = Question(
            text="Que curso es el mejor aplicado?", date=time)
        self.assertIs(past_question.was_published_recently(), False)

    def test_was_published_recently_with_present_questions(self):
        """was_published_recently returns True for questions whose date is in the present(1 day)"""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        present_question = Question(
            text="Que curso es el mejor aplicado?", date=time)
        self.assertIs(present_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a question with the given "question_text" and published the
    given number of days offset to now (negative for questions published in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(text=question_text, date=time) #Crea la pregunta en la BDD de pruebas que tiene django


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """if no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse(
            "polls:index"))  # self.cliente modulo de django que permite hacer peticiones http
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_no_future_question(self):
        response = self.client.get(reverse("polls:index"))
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(text="future question", date=time)
        self.assertNotIn(
            future_question, response.context["latest_question_list"])

    def test_past_question(self):
        question = create_question(question_text="Past question", days=-10)    #Creo la question en la BDD de pruebas 
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question]) #Me fijo que la question este en el index
    
    def test_future_and_past_question(self):
        past_question = create_question(question_text="Past question",days=-30)
        future_question = create_question(question_text="Future question",days=30)
        response = self.client.get(reverse("polls:index"))  #Pedir el response despues de crear las preguntas
        self.assertQuerysetEqual(response.context["latest_question_list"],[past_question])


    def test_two_past_questions(self):
        past_question1 = create_question(question_text="Past question",days=-30)
        past_question2 = create_question(question_text="Past question ",days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"] ,[past_question1,past_question2])

    def test_two_future_questions(self):
        past_question1 = create_question(question_text="Future question",days=30)
        past_question2 = create_question(question_text="Future question ",days=40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"] ,[])
    

