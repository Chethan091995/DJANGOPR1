from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>WELCOME</h1>")
def fruits(request):
    fru=["Apple","Mango","Orange"]
    return render(request,"fruits.html",context={"fruits":fru})

def greater(request):
    return render(request,"directory/greater.html",{"a":30,"b": 20})