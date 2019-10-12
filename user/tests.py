from django.test import TestCase
from .models import User


class ModelTest(TestCase):

    def setUp(self):
        user = User(email='test@mail.ru', password='test213', first_name='Jack', last_name='Jack')
        user.save()
        user = User.objects.get(email='test@mail.ru')
        print(user)


