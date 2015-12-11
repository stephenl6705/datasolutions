from django.db import models

class Topic(models.Model):
    title = models.TextField(default='')
    text = models.TextField(default='')