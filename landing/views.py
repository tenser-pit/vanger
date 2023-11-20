from django.shortcuts import render

from .models import Image


def landing_render(request):
    slider = Image.objects.all()
    return render(request, 'index.html', {'slider': slider})

