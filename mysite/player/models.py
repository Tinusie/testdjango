from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Player(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=200, null=True)
    name = models.TextField(blank=True, null=True)
    club = models.TextField(blank=True, null=True)
    team = models.TextField(blank=True, null=True)
    age = models.CharField(max_length=110, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title