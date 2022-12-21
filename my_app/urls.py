from django.contrib import admin
from django.urls import path
from Music.views import AddNewAlbum, AllSongs, AlbumDetails, Home, ContactUs, AlbumDetails, Login, Logout, Signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login, name="login"),
    path('logout', Logout, name="logout"),
    path('signup', Signup, name="signup"),
    path('home/', Home, name="home"),
    path('all-new-album', AddNewAlbum, name="add-album"),
    path('songs', AllSongs , name='songs'),
    path('details-of-album/<int:aId>/', AlbumDetails, name="album_details"),
    path('connect/', ContactUs),
]



