from django.shortcuts import render
from . models import *

from django import forms
from django.shortcuts import redirect, render
from . forms import ContactForm
# Create your views here.

def main(request):
    about = About.objects.all()
    testimonial = Testimonials.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    work = Work.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'about':about,
        'testimonial':testimonial,
        'education':education,
        'experience':experience,
        'work':work,
        'form': form
    }
    return render(request, 'index.html', context)


