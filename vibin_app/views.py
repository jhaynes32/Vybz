from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

from .models import Artist, Song, Friend
from .forms import ArtistForm, SongForm
# Create your views here.

def home(request):
  return HttpResponse("Goodbye rocket ship. Hello Home.")

def api_artists(request):
  all_artists = Artist.objects.all()
  data = []
  for artist in all_artists:
    data.append({"name": artist.name, "nationality":artist.nationality})
  return JsonResponse({"data":data, "status":200})

def artist_list(request):
  artists = Artist.objects.all()
  context = {"artists":artists}
  return render(request, 'artist_list.html', context)

def artist_detail(request,pk):
  artist = Artist.objects.get(id=pk)
  context = {"artist":artist}
  return render(request, 'artist_detail.html', context)

@login_required
def artist_create(request):
  if request.method == 'POST':
    form = ArtistForm(request.POST)
    if form.is_valid(): 
      artist = form.save(commit=False)
      artist.user = request.user
      artist.save()
      request.user.artists.add(artist)
      return redirect('artist_detail', pk=artist.pk)
  else: 
    form = ArtistForm()
  context = {'form': form, 'header': "Add New Artist"}
  return render(request, 'artist_form.html', context)

@login_required
def artist_edit(request, pk):
  artist = Artist.objects.get(id=pk)
  if request.method == 'POST':
    form = ArtistForm(request.POST, instance=artist)
    if form.is_valid():
      artist = form.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = ArtistForm(instance=artist)
  context = {'form': form, 'header': f"Edit {artist.name}"}
  return render(request, 'artist_form.html', context)

@login_required
def artist_delete(request, pk):
  Artist.objects.get(id=pk).delete()
  return redirect('artist_list')

@login_required
def song_create(request, pk):
  artist = Artist.objects.get(id=pk)
  if request.method == 'POST':
    form = SongForm(request.POST)
    if form.is_valid():
      song = form.save(commit=False)
      song.artist = artist
      song.save()
      return redirect('artist_detail', pk=song.artist.pk)
  else: 
    form = SongForm()
  context = {'form': form, 'header':f"Add song for {artist.name}", "artist":artist}
  return render(request, 'song_form.html', context)

@login_required
def song_edit(request,pk,song_pk):
  song = Song.objects.get(id=song_pk)
  if request.method == 'POST':
    form = SongForm(request.POST, instance=song)
    if form.is_valid():
      song = form.save()
      return redirect('artist_detail', pk=song.artist.pk)
  else:
    form = SongForm(instance=song)
  context = {'form':form, 'header': f"Edit {song.title} by {song.artist.name}", "artist":song.artist}
  return render(request, 'song_form.html', context)

@login_required
def song_delete(request, pk, song_pk):
  Song.objects.get(id=song_pk).delete()
  return redirect('artist_detail', pk=pk)

def song_list(request):
  songs = Song.objects.all()
  context = {"songs":songs}
  return render(request, 'song_list.html', context)



def song_detail(request, id):
    song = Song.objects.get(id=id)
    context = {"song":song}
    return render(request, 'song_detail.html', context) 



def profile(request):
  artists = Artist.objects.filter(user=request.user)
  users = User.objects.all()
  friend = Friend.objects.get(current_user=request.user)
  friends = friend.users.all()
  context = {'artists':artists, 'users': users, 'friends': friends}
  return render(request, 'profile.html', context)

# def profile(request, pk):
#   user = User.objects.get(id=pk)
#   friend = Friend.objects.get(current_user=request.user)
#   context = {'user': user, 'friends': friends}
#   return render(request, 'profile.html', context)
 