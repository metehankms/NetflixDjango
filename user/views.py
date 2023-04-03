from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from movies.views import *
from .form import *
# Create your views here.

def register(request):
    return render(request,"register.html")

def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("profiles")
        else:
            return render(request,"login.html")
    return render(request,"login.html")


def createProfil(request):
    form = ProfilForm()
    if request.method == "POST":
        form = ProfilForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.owner=request.user
            profile.save()
            return redirect("profiles")
    context = {
        'form' : form
    }
    return render(request,"create-profil.html",context)


def oturumKapat(request):
    logout(request)
    return redirect("anasayfa")

def userProfil(request):
    profil=request.user
    context={
        "profil":profil
    }
    return render(request,"hesap.html",context)


def deleteUser(request):
    profil =request.user
    profil.delete()
    return redirect("anasayfa")