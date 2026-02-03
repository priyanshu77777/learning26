from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"student\demo.html")

def studentdetails(request):
    data= { "name":"Rahul","age":20,"result":"pass"}
    return render(request,"student\studentdetails.html",data)