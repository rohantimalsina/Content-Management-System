from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

#Home Page
def home(request):
	return render(request,'home.html')

#Admin Login
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect("/")

		else:
			messages.info(request,'invalid credentials')
			return redirect('login')

	else: 
		return render(request,'login.html')












#Courses
def courses(request):
	return render(request,'courses.html')

#Events
def events(request):
	return render(request,'events.html')

#Galleries
def galleries(request):
	return render(request,'galleries.html')
