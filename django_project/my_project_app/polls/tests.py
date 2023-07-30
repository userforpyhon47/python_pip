import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionTest(TestCase):
    """Test if questions pub_date is within a day"""
    def test_pub_date(self): # test methods must start with test_
        question = Question(question_text="Test message", pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertFalse(question.published_recently())


class QuestionIndexViewTest(TestCase):
    """Test question in the index view"""
    def test_no_questions(self): # test methods must start with test_
        """Test if no questions page is displayed correctly"""
        result = self.client.get(reverse("polls:index"))
        self.assertEqual(result.status_code, 200)
        self.assertContains(result, "available")
        self.assertQuerysetEqual(result.context["question_list"], [])

    def test_no_future_questions(self): # test methods must start with test_
        """Test if future questions are not displayed"""
        Question.objects.create(question_text="Future Question 1", pub_date=timezone.now() + datetime.timedelta(days=30))
        Question.objects.create(question_text="Future Question 2", pub_date=timezone.now() + datetime.timedelta(days=40))
        result = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(result.context["question_list"], [])
    
    def test_past_questions(self): # test methods must start with test_
        """Test if past questions are not displayed"""
        q1 = Question.objects.create(question_text="Past Question 1", pub_date=timezone.now() - datetime.timedelta(days=30))
        q2 = Question.objects.create(question_text="Past Question 2", pub_date=timezone.now() - datetime.timedelta(days=40))
        result = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(result.context["question_list"], [q1, q2])

class QuestionDetailViewTest(TestCase):
    """Test question in the detail view"""
    def test_future_questions(self): # test methods must start with test_
        """Test if the detail of future questions are not displayed"""
        question = Question.objects.create(question_text="Future Question 1", pub_date=timezone.now() + datetime.timedelta(days=30))
        result = self.client.get(reverse("polls:detail", args=(question.id,)))
        self.assertEqual(result.status_code, 404)