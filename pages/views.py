from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth	
from django.core.mail import send_mail
from Gallery.models import summer,campus,tour
from Events.models import newevent
from Contact.models import Contact
from Bit.models import bit_Year_1,bit_Year_2,bit_Year_3
from Bibm.models import bibm_Year_1,bibm_Year_2,bibm_Year_3,bibm_Year_4

# Create your views here.

#Home Page
def home(request,*args,**kwargs):
	return render(request,"home.html")

#Courses
def bit(request,*args,**kwargs):
	bit_obj=bit_Year_1.objects.all()
	bit_obj_2=bit_Year_2.objects.all()
	bit_obj_3=bit_Year_3.objects.all()

	return render(request,"bit.html",{"bit_Year_1":bit_obj,"bit_Year_2":bit_obj_2,"bit_Year_3":bit_obj_3})

def bibm(request,*args,**kwargs):
	bibm_obj=bibm_Year_1.objects.all()
	bibm_obj_2=bibm_Year_2.objects.all()
	bibm_obj_3=bibm_Year_3.objects.all()
	bibm_obj_4=bibm_Year_4.objects.all()

	return render(request,"bibm.html",{"bibm_Year_1":bibm_obj,"bibm_Year_2":bibm_obj_2,"bibm_Year_3":bibm_obj_3,"bibm_Year_4":bibm_obj_4})
def events(request):
	events_obj=newevent.objects.all()
	return render(request,"events.html",{"newevent":events_obj})

#Galleries
def galleries(request,*args,**kwargs):
	return render(request,"galleries.html")


#Camp
def camp(request,*args,**kwargs):
	galleries_obj=summer.objects.all()
	return render(request,"camp.html",{"summer":galleries_obj})

#College
def college(request,*args,**kwargs):
	galleries_obj2=campus.objects.all()
	return render(request,"college.html",{"campus":galleries_obj2})

#Exposure
def exposure(request,*args,**kwargs):
	galleries_obj3=tour.objects.all()
	return render(request,"exposure.html",{"tour":galleries_obj3})

#contact
def contactpage(request,*args,**kwargs):
	if request.method == 'POST':
		contact=Contact()
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		message=request.POST.get('message')
		contact.name=name
		contact.email=email
		contact.subject=subject
		contact.message=message
		contact.save()

		
		return render(request,'contact.html',{'name':name})

	else:
		return render(request,"contact.html",{})	
			
        
		
		
        
		
		
        
	
		
	
