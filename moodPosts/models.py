from django.conf import settings
from django.db import models

# Create your models here.

class Moodposts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name="user")
    mood = models.CharField(max_length=120, null=False)

    @property
    def owner(self):
        return self.user
