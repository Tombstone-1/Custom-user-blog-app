from django.shortcuts import render, redirect
from .forms import create_post_form

from .models import recipes

# Create your views here.
def home(request):
    data = recipes.objects.all()
    
    context = {'data' : data}
    return render(request, 'posts/home.html', context)

def create_post(request):
    form = create_post_form()

    if request.method  == 'POST':
        form = create_post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("/create_post")
    
    context = {'post_form' : form}
    return render(request, 'posts/create_post.html', context)

def update_post(request, pk):
    query = recipes.objects.get(id = pk)
    form = create_post_form(instance=query)

    if request.method == 'POST':
        form = create_post_form(request.POST, instance=query)

        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("/")
    
    context = {'update_post' : form}
    return render(request, 'posts/update_post.html', context)

def delete_post(request, pk):
    query = recipes.objects.get(id = pk)
    if request.method == 'POST':
        if query is not None:
            query.delete()
            return redirect("/")
        else:
            return redirect("/")

    
    context = {}  
    return render(request, 'posts/delete_post.html', context)