from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("aboutus")

def contact(request):
    return render(request, 'contact.html')

def recipe(request):
    ingredients = ["Aloo","spices"]
    data = {"name":"Aloo paratha","time":30,"ingredients":ingredients}
    return render(request,"recipe.html",data)

def teams(request):
    teamplayers = ["Virat Kohli","Rajat Patidar","Phil Salt"]
    data = {"teamname":"RCB","teambanfor":"2","JerseyColour":"red","captain":"Rajat Patidar","teamplayers":teamplayers}
    return render(request,"teams.html",data)

def gymplan(request):
    necessary_things = ["Diet","Proper Sleep","Exercise","Recovery"]
    data = {"workoutat":"gym","goal":"Proper Physique","calories_burned":"500","necessarythings":necessary_things}
    return render(request,"gymplan.html",data)