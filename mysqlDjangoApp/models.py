from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0, null=False, blank=False)
    lastupdate = models.DateTimeField(auto_now=True)
