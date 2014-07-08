from django.db import models

# Create your models here.


class Servo(models.Model):
    position = models.SmallIntegerField()