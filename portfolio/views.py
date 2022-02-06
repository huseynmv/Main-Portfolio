from django.shortcuts import render
from . models import *
# Create your views here.

def main(request):
    about = About.objects.all()
    context = {
        'about':about
    }
    return render(request, 'index.html', context)