from django.shortcuts import render
from home import models

# Create your views here.
def home(request):
    return render(request, "home.html")
def donate(request):
    if request.method=="POST":
        #print("this is post")
        name=request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        type_of_donation = request.POST["type_of_donation"]
        #print(name,phone,email,type_of_donation)
        donatetable=models.donatetable(name=name, phone=phone,email=email, type_of_donation=type_of_donation)
        donatetable.save()
        #print("Data has been stored")
    return render(request, "donate.html")
def request(request):
    if request.method=="POST":
        #print("this is post")
        name=request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        type_of_donation = request.POST["type_of_donation"]
        #print(name,phone,email,type_of_donation)
        requesttable =models.requesttable(name=name, phone=phone,email=email, type_of_donation=type_of_donation)
        requesttable.save()
        #print("Data has been stored")
    return render(request, "request.html")