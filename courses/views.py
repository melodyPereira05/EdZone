from django.shortcuts import render
from django.http import HttpResponse
from math import ceil


# Create your views here.

def home(request):     
    return render(request,'home.html',context)
 
def about(request):
    return render(request,'about.html')

def contact_us(request):
    return render(request,'contact_us.html')
