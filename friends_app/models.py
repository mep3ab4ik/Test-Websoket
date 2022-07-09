from django.db import models
from django.conf import settings


class Friend(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    is_accepted = models.BooleanField(default=False)
    wait_answer = models.BooleanField(default=True)

    class Meta:
        unique_together = [('sender', 'receiver'), ('receiver', 'sender')]
