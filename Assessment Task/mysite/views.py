from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

def index(request):
	users = User.objects.all()  #grab all users from the user model
	return render_to_response('index.html', {'users':users}, RequestContext(request))  #send information to requesting page

def about(request):
	return render_to_response('about.html', RequestContext(request))  #respond with location of about page