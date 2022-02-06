from django.shortcuts import render
from . models import *
# Create your views here.

def main(request):
    about = About.objects.all()
    testimonial = Testimonials.objects.all()
    context = {
        'about':about,
        'testimonial':testimonial
    }
    return render(request, 'index.html', context)