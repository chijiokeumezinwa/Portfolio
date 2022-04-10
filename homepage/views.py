from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
			email_message = form.cleaned_data['message']
			send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS, fail_silently=False)
			return render(request, 'success.html')
		else:
			return HttpResponse("form is not validated")
	form=ContactForm()
	context = {'form': form}
	return render(request, 'index.html', context)
