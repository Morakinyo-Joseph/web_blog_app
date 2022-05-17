from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Blog(models.Model):
    headline = models.CharField(max_length=250)
    content = models.CharField(max_length=2050)
    time_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.headline
