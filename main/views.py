from django.shortcuts import render
from .models import Category, Post

# Main page
def home(request):
    return render(request, 'main/index.html')

def blog(request):
    return render(request, 'main/pages/blog.html', {'post': Post.objects.all()} )

# Category  pages
def lifestyle(request):
    lifestyle = Category.objects.get(id=1)
    post = lifestyle.post_set.all()
    return render(request, 'main/categories/lifestyle.html', {'post': post})

def nature(request):
    nature = Category.objects.get(id=2)
    post = nature.post_set.all()
    return render(request, 'main/categories/nature.html', {'post': post})

def creative(request):
    creative = Category.objects.get(id=3)
    post = creative.post_set.all()
    return render(request, 'main/categories/creative.html', {'post': post})

def motivation(request):
    motivation = Category.objects.get(id=4)
    post = motivation.post_set.all()
    return render(request, 'main/categories/motivation.html', {'post': post})

def inspiration(request):
    inspiration = Category.objects.get(id=5)
    post = inspiration.post_set.all()
    return render(request, 'main/categories/inspiration.html', {'post': post})

def travel(request):
    travel = Category.objects.get(id=6)
    post = travel.post_set.all()
    return render(request, 'main/categories/travel.html', {'post': post})

# Authentication
def register(request):
    return render(request, 'main/pages/registr.html')

def login(request):
    return render(request, 'main/pages/signin.html')











