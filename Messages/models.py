from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name="sent_messages")
    Receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name="received_messages")
    Subject = models.CharField(max_length=50)
    Message = models.TextField()
    creation_Date = models.DateField(auto_now=True)
    Read = models.BooleanField(default=False)
    Sender_Delete = models.BooleanField(default=False)
    Receiver_Delete = models.BooleanField(default=False)

    def __str__(self):
        return self.Subject + ' ' + str(self.creation_Date)

