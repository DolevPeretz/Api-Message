from django.test import TestCase
import datetime
from django.test import tag
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
import json
from Messages.models import Message

class MessagesTestCase(APITestCase):

    def test_perform_create(self):
        super().setUp()
        self.client = APIClient()
        Resgisteer1 = {"email": "Test1@gmail.com",
                 "username": "test1",
                 "password": "123456A!",
                 "password2": "123456A!"}
        Resgisteer2 = {"email": "Test2@gmail.com",
                 "username": "test2",
                 "password": "123456A!",
                 "password2": "123456A!"}
        Resgisteer3 = {"email": "Test3e@gmail.com",
                 "username": "test3",
                 "password": "123456A!",
                 "password2": "123456A!"}
        self.user1 = User.objects.create_user(Resgisteer1)
        self.user2 = User.objects.create_user(Resgisteer2)
        self.user3 = User.objects.create_user(Resgisteer3)
        self.user1.save()
        self.user2.save()
        self.user3.save()
        self.msg1 = Message.objects.create(sender=self.user1,
                                      Receiver=self.user2,
                                      Subject='msg1',
                                      Message='msg1',
                                      creation_Date=datetime.date.today())
        self.msg2 = Message.objects.create(sender=self.user3,
                                      Receiver=self.user2,
                                      Subject='msg2',
                                      Message='msg2',
                                      creation_Date=datetime.date.today())
        self.msg3 = Message.objects.create(sender=self.user1,
                                      Receiver=self.user2,
                                      Subject='msg3',
                                      Message='msg3',
                                      creation_Date=datetime.date.today())
        self.msg1.save()
        self.msg2.save()
        self.msg3.save()




