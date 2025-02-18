from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from music.models import Album, Musician

def index(request):
    artists = Musician.objects.all()
    return render(request, 'index.html', {'artists': artists})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Musician, pk=artist_id)
    albums = Album.objects.filter(artist=artist)
    return render(request, 'artist_detail.html', {'artist': artist, 'albums': albums})

def add_album(request, artist_id):
    artist = get_object_or_404(Musician, pk=artist_id)
    if request.method == "POST":
        title = request.POST.get("title")
        release_date = request.POST.get("release_date")
        num_stars = request.POST.get("num_stars")

        if title and release_date and num_stars:
            Album.objects.create(title=title, artist=artist, release_date=release_date, num_stars=num_stars)
            messages.success(request, "Album created")
        else:
            messages.error(request, "Error: All fields are required")

        return redirect("artist_detail", artist_id=artist.id)
    
    return render(request, "add_album.html", {"artist": artist})

def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    artist_id = album.artist.id
    album.delete()
    messages.warning(request, f"Album {album.title} deleted")
    return redirect("artist_detail", artist_id=artist_id)
