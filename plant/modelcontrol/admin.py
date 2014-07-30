# -*- coding: utf-8 -*-
from django.contrib import admin
from modelcontrol.models import Servo, Motor, Plant

admin.site.register(Servo)
admin.site.register(Motor)
admin.site.register(Plant)