from django.db import models
from django.conf import settings
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creator')
    current_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='current_user')

    def __str__(self):
        return f'Room({self.name} - author {self.creator}'


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='message')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='message')
    text = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message({self.room}, {self.user})'
