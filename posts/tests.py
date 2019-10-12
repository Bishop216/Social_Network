from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from .views import home, createpost, postpreference


class ViewTests(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()
        self.user = get_user_model().objects.create_user(email='test@mail.ru', password='test213', first_name='Jack',
                                                         last_name='Jack')

    def test_post(self):
        request = self.request_factory.post(reverse(createpost), {'title': 'test', 'content': 'test'})
        request.user = self.user
        response = createpost(request)
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        request = self.request_factory.get(reverse(home))
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_postfreference(self):
        request = self.request_factory.post(reverse(postpreference))
        request.user = self.user
        response = postpreference(request, 1, 1)
        self.assertEqual(response.status_code, 200)
