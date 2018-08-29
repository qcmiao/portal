# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.models import BaseModel

# Create your models here.


class Department(BaseModel):
	department_name = models.CharField(max_length=40, unique=True)


class AppUrl(BaseModel):
	app_name = models.CharField(max_length=40, unique=True)
	app_url = models.CharField(max_length=40, null=True)