# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse

from django.shortcuts import render

# Create your views here.


def homepage(request):
    return HttpResponse("Hello World!")
