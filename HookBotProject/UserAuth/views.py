from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    # Add logic for your home view
    context={}
    return render(request,'UserAuth/login.html',context) 

