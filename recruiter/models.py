from django.db import models
from django.utils import timezone

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    html = models.IntegerField(default=0)
    css = models.IntegerField(default=0)
    javascript = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    django = models.IntegerField(default=0)
    ios = models.IntegerField(default=0)
    android = models.IntegerField(default=0)
    published_date = models.DateTimeField(default=timezone.now)

    def apply(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name