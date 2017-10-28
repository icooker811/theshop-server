# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from products.models import Product


def homepage(request):
    products = Product.objects.all()[:9]
    return render(request, 'pages/index.html', {'user': request.user, 'products': products})
