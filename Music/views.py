from django.shortcuts import render,redirect
from django.http import HttpResponse
from Music.models import Albums, Songs
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def Home(request):
     if not request.user.is_authenticated:   #open in private windows example incognito
          return redirect('login')


     # print(request.user,"User")
     allAlbums = Albums.objects.all()
     my_list={'title':"Welcome to my Music Application",'fee':'1200', 'albums':allAlbums}
     return render(request,"home.html",my_list)
          


def AlbumDetails(request, aId):
    album = Albums.objects.filter(id = aId).first()
    albumSongs = Songs.objects.filter(albumName = album)
    return render(request, "details.html", {"album":album, "songs":albumSongs}) 


def AddNewAlbum(request):
     if request.method == "POST":
          formData = request.POST
          title = formData["title"]
          artist = formData["artist"]

          album = Albums()
          album.title = title
          album.artist = artist
          album.save()

          return redirect('home')


          
     return render(request, 'addAlbum.html')


def AllSongs(request):
     allSongs = Songs.objects.all()
     return render(request,"Songs.html", {'songs':allSongs})


def ContactUs(request):
    return render(request, "connect.html")  


def Login(request):
     if  request.user.is_authenticated:
          return redirect('home')
     isError = False
     if request.method =="POST":
          data = request.POST
          UserName = data['username']
          Pass = data['password']

          usr = authenticate(username= UserName, password = Pass)
          if usr:
               login(request, usr)
               return redirect('home/')
          isError = True     


     return render(request,"login.html", {"error":isError}) 


def Signup(request):
     if request.method == "POST":
          data = request.POST
          #print(data)
          UserName = data['username']
          Pass = data['password']
          Email = data['email']

          # usr = User()
          # usr.username = UserName
          # usr.email = Email
          # usr.password = Pass
          # usr.save()

          usr = User.objects.create_user(UserName,Email, Pass)
          return redirect('login')
     return render(request,"signup.html")        


def Logout(request):
     logout(request)
     return redirect('login')

   