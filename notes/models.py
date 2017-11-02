# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
 
class Note(models.Model):
    text = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    