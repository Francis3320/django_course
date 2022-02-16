from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse("Welcome to my homepage")
   return render(request, 'homepage.html')

def about(request):
    #return HttpResponse("about")
    return render(request,'about.html')

def articles_list(request):
   return render(request,'')