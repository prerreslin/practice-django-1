from django.shortcuts import render, get_object_or_404
from music.models import Album, Musician

def index(request):
    artists = Musician.objects.all()
    return render(request, 'index.html', {'artists': artists})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Musician, pk=artist_id)
    albums = Album.objects.filter(artist=artist)
    return render(request, 'artist_detail.html', {'artist': artist, 'albums': albums})
