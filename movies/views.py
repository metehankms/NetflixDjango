from django.shortcuts import render
from .models import *
from user.models import Profiles
from django.db.models import Q
# Create your views here.

def anasayfa(request):
    return render(request,"index.html")

def hesap(request):
    return render(request,"hesap.html")



def video(request):
    return render(request,"video.html")

def profiles(request):
    kullanicilar=Profiles.objects.filter(owner=request.user)
    context={
        "kullanici":kullanicilar
    }
    return render(request,"browse.html",context)

def browse_index(request):
    filmler=Movies.objects.all()
    search_movi=""
    if request.GET.get("search_movie"):
        search_movi=request.GET.get("search_movie")
        filmler=filmler.filter(
            Q(filmismi__icontains=search_movi) |
            Q(kategori__name__icontains=search_movi) 
            # Q(tur__name__icontains=search_movi)
            )

    try:
        izleyen=Izlenenler.objects.get(user=request.user)
        izlenen=izleyen.izlenen.all()
        context={
            "izlenen":izlenen,
            "filimler":filmler,
            "search_movie":search_movi,
        }
        return render(request,"browse-index.html",context)
    except:
        context={
            "filimler":filmler,
            "search_movie":search_movi,
        }
        return render(request,"browse-index.html",context)
    


