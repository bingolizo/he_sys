from django.db import models

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.date_time}"
