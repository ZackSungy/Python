# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Business(models.Model):
    num=models.CharField(max_length=20);
    name=models.CharField(max_length=30,primary_key=True);
    call=models.CharField(max_length=20);
    rem=models.CharField(max_length=30);
    def __unicode__(self):
        return self.name


class Order(models.Model):
    name=models.CharField(max_length=20);
    momey=models.CharField(max_length=10);
    Business=models.ForeignKey(Business);
    def __unicode__(self):
        return self.name


class Bill(models.Model):
    paper=models.CharField(max_length=20);
    sq=models.TextField(null=True);
    money=models.CharField(max_length=20);
    def __unicode__(self):
        return self.paper

