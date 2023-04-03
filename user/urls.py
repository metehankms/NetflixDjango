from django.urls import path
from .views import*

urlpatterns = [
    path('login/',userLogin,name = "login"),
    path('register/',register,name = "register"),
    path('create-profil/',createProfil,name="create-profil"),
    path('logout',oturumKapat,name="logout"),
    path('hesap/',userProfil,name="hesap"),
    path('delete',deleteUser,name="delete")
]