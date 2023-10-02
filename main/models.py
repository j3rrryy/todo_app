from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    priority = models.FloatField(default=1.0)
    creation_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def priority_validator(self):
        if self.priority < 0:
            self.priority = 0.0
        elif self.priority > 1:
            self.priority = 1.0

    def save(self, *args, **kwargs):
        self.priority_validator()
        return super().save(*args, **kwargs)
