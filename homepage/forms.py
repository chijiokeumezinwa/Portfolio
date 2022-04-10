from django.forms import ModelForm,TextInput,EmailInput, Textarea
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
        	'name': TextInput(attrs={'id': 'inputName', 'class':'form-control', 'placeholder':'Enter your name'}),
        	'email': EmailInput(attrs={'id': 'inputEmail','class':'form-control', 'placeholder':'Enter your email'}),
        	'subject': TextInput(attrs={'id': 'inputSubject', 'class':'form-control', 'placeholder':'Enter your subject'}),
        	'message': Textarea(attrs={'id': 'inputMessage', 'class':'form-control', 'placeholder':'Enter your Message', 'style':'height: 12rem;'}),
        }
