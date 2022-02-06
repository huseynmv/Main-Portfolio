from django.shortcuts import render
from . models import *
# Create your views here.

def main(request):
    about = About.objects.all()
    testimonial = Testimonials.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    work = Work.objects.all()
    
    context = {
        'about':about,
        'testimonial':testimonial,
        'education':education,
        'experience':experience,
        'work':work
    }
    return render(request, 'index.html', context)