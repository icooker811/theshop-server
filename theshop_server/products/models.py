# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.category_name


class ProductCompany(models.Model):
    name = models.CharField(max_length=75)
    address = models.TextField()

    def __unicode__(self):
        return self.name


class ProductBrand(models.Model):
    name = models.CharField(max_length=75)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    teaser = models.CharField(max_length=500)
    description = models.TextField()

    search_text = models.TextField()

    category = models.ForeignKey(ProductCategory)
    company = models.ForeignKey(ProductCompany)
    brand = models.ForeignKey(ProductBrand)

    offer_value = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)

    published_at = models.DateTimeField('date published')

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
