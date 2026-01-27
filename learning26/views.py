from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("aboutus")

def contact(request):
    return render(request, 'contact.html')
