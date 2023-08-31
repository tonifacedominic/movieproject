from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . form import Movieform

# Create your views here.
def index (request):
    movies=movie.objects.all()
    content={'movie_list':movies}
    return render(request, 'index.html', content)

def detail (request,movie_id):
    detail=movie.objects.get(id=movie_id)
    return render(request, 'detail.html',{'detail':detail})

def add_movie(request):
    if request.method=="POST":

        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        image=request.FILES['img']
        add_movie=movie(name=name, desc=desc,year=year,image=image)
        add_movie.save()

    return render(request,'add_movie.html')

def update(request, id):

    upmovie= movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES, instance=upmovie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html',{'upmovie':upmovie, 'form':form})

def delete(request,id):
    if request.method=='POST':
        deletemovie=movie.objects.get(id=id)
        deletemovie.delete()
        return redirect('/')
    return render(request,'delete.html')






