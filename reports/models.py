from django.db import models

class Topic(models.Model):
    text = models.TextField(default='')