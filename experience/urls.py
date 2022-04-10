from django.urls import path
from . import views

urlpatterns = [
	path("",views.experience_index, name="experience_index"),
]