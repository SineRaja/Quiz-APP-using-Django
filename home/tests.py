from cgi import test
from http.client import responses
from django import forms
from django.db import IntegrityError
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from django.db import models


from django.contrib.auth.models import User, AnonymousUser

from . import views

# Create your tests here.       

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'sineraja',
            'password': 'raja123'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


class LogInTestFour(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'ramraja',
            'password': 'ram1234'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

class AuthenticationTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='sineraja')

    def test_user_created(self):
        user = User.objects.filter(username='sineraja')
        self.assertTrue(user.exists())


class AuthenticationTestCaseTwo(TestCase):
    def setUp(self):
        User.objects.create(username='rajasine')

    def test_user_created(self):
        user = User.objects.filter(username='sinerja')
        self.assertFalse(user.exists())


class AuthenticationTestCaseThree(TestCase):
    def setUp(self):
        User.objects.create(username='sineraja')

    def test_user_created(self):
        user = User.objects.filter(username='sinerja')
        self.assertFalse(user.exists())


class AuthenticationTestCaseFour(TestCase):
    def setUp(self):
        User.objects.create(username='rajasine')

    def test_user_created(self):
        user = User.objects.filter(username='rajasine')
        self.assertTrue(user.exists())