from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'title':"WOW I am your first webpage"}
    return render(request,'website_app/index.html',context=my_dict)