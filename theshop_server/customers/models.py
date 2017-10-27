# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CustomerProfile(models.Model):
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()

    user = models.OneToOneField(User)

