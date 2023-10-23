from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class GameScore(models.Model):
    player = models.ForeignKey(User,primary_key=True ,on_delete=models.CASCADE)
    score = models.IntegerField()
    played_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-played_on']  # Order by played_on descending

# Create your models here.
