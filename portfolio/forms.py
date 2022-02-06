from django import forms
from .models import Contact
from django.db.models import fields

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Name...'}),
             'subject': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Subject...'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Your Message...'})
        }