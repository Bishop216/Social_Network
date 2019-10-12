from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from . import views
from django.urls import reverse


class ModelTest(TestCase):

    def user_creation(self):
        self.request_factory = RequestFactory()
        self.user = get_user_model().objects.create_user(email='test@mail.ru', password='test213', first_name='Jack',
                                                         last_name='Jack')

class ViewTest(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()
        self.user = get_user_model().objects.create_user(email='test@mail.ru', password='test213', first_name='Jack',
                                                         last_name='Jack')

    def test_authenticate(self):
        request = self.request_factory.post(reverse(views.authenticate_user))
        request.user = self.user
        response = views.authenticate_user(request)
        self.assertEqual(response.status_code, 200)


