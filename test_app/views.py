from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_index(request):
    return render(request, "test_app/index.html")

def masum(request):
    return HttpResponse("hello from masum")

def greetings(request, name):
    return HttpResponse(f"hello from , {name}")

def greet(request, user_name):
    return render(request,"test_app/greet.html",{
        "user_name" : user_name.capitalize()
    })