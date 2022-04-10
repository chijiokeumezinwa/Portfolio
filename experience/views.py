from django.shortcuts import render
from experience.models import Course, School, Experience

# Create your views here.
def experience_index(request):
	courses = Course.objects.all()
	schools = School.objects.all()
	# schools=School.objects.get(name_of_school__exact="Lehigh University")
	experiences = Experience.objects.all()
	context = {
		'courses': courses,
		'schools': schools,
		'experiences': experiences,
	}
	return render(request, 'experience_index.html', context)
