from django.db.models import CASCADE
from django.utils import timezone

from django.db import models


class MailingList(models.Model):
    mailing_launch_datetime = models.DateTimeField()
    mailing_end_datetime = models.DateTimeField()
    text = models.TextField(max_length=255)
    tag = models.CharField(max_length=60)
    code = models.CharField(max_length=4)


class Client(models.Model):
    number = models.PositiveIntegerField()
    code = models.CharField(max_length=4)
    tag = models.CharField(null=True, max_length=20)
    timezone = models.CharField(max_length=10)


class Message(models.Model):
    STATUS_OPTIONS = (
        ('S', 'Successfully'),
        ('F', 'Failed'),
    )
    send_datetime = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)
    mailing_list = models.ForeignKey(MailingList, on_delete=CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=CASCADE, related_name='messages')