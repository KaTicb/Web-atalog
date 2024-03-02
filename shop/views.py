from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    items = models.Item.objects.all()
    return render(request, 'courses.html', {'items': items})
