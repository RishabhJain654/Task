from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Tracks, Genres
from .forms import TrackForm, GenreForm
import django_filters

class TrackFilter(django_filters.FilterSet):
    class Meta:
        model = Tracks
        fields = {
            'title': ['contains'],
            'genre': ['contains'],
        }

class GenreFilter(django_filters.FilterSet):
    class Meta:
        model = Genres
        fields = {
            'name': ['contains'],
        }

def home(request):
    return render(request,'musicapp/home.html')

def new(request):
    return render(request,'musicapp/new.html')

def tracks_list(request):
    tracks = Tracks.objects.order_by('title')
    paginator = Paginator(tracks, 5)
    page = request.GET.get('page')
    try:
        tracks = paginator.page(page)
    except PageNotAnInteger:
        tracks = paginator.page(1)
    except EmptyPage:
        tracks = paginator.page(paginator.num_pages)
    return render(request,'musicapp/tracks_list.html',{'tracks':tracks})

def tracks_detail(request,pk):
    track = get_object_or_404(Tracks, pk=pk)
    return render(request, 'musicapp/tracks_detail.html', {'track':track})

def new_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save()
            return redirect('tracks_detail', pk=track.pk)
    else:
        form = TrackForm()
        return render(request, 'musicapp/track_edit.html', {'form':form})

def track_edit(request,pk):
    track = get_object_or_404(Tracks, pk=pk)
    if request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            track = form.save()
            return redirect('tracks_detail', pk=track.pk)
    else:
        form = TrackForm(instance=track)
        return render(request, 'musicapp/track_edit.html', {'form':form})

def genres_list(request):
    genres = Genres.objects.order_by('name')
    paginator = Paginator(genres, 5)
    page = request.GET.get('page')
    try:
        genres = paginator.page(page)
    except PageNotAnInteger:
        genres = paginator.page(1)
    except EmptyPage:
        genres = paginator.page(paginator.num_pages)
    return render(request,'musicapp/genres_list.html',{'genres':genres})

def genre_detail(request,pk):
    genre = get_object_or_404(Genres, pk=pk)
    return render(request, 'musicapp/genre_detail.html', {'genre':genre})

def new_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            return redirect('genre_detail', pk=genre.pk)
    else:
        form = GenreForm()
        return render(request, 'musicapp/genre_edit.html', {'form':form})

def genre_edit(request,pk):
    genre = get_object_or_404(Genres, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            genre = form.save()
            return redirect('genre_detail', pk=genre.pk)
    else:
        form = GenreForm(instance=genre)
        return render(request, 'musicapp/genre_edit.html', {'form':form})

def search_track(request):
    track_list = Tracks.objects.order_by('title')
    track_filter = TrackFilter(request.GET, queryset=track_list)
    return render(request, 'musicapp/track_search.html', {'filter': track_filter})

def search_genre(request):
    genre_list = Genres.objects.order_by('name')
    genre_filter = GenreFilter(request.GET, queryset=genre_list)
    return render(request, 'musicapp/genre_search.html', {'filter': genre_filter})
