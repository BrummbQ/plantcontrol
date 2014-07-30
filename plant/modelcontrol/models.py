from django.db import models

# Create your models here.


class Servo(models.Model):
    position = models.SmallIntegerField()
    gpio = models.SmallIntegerField()


class Motor(models.Model):
    speed = models.SmallIntegerField()
    gpio = models.SmallIntegerField()


class Plant(models.Model):
    servo = models.ForeignKey(Servo)
    motor = models.ForeignKey(Motor)

