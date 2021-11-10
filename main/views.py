from django.shortcuts import redirect, render
from .models import Category, Post
from django.core.paginator import Paginator
from django.views.generic import  ListView
# Main page
def home(request):
    return render(request, 'main/index.html')


# def blog(request):
#     return render(request, 'main/pages/blog.html', {'post': Post.objects.all()})

class BlogListView(ListView):
    model = Post
    template_name = 'main/pages/blog.html' 
    context_object_name = 'post'
    paginate_by = 2


def post_detail(request, pk):
    return render(request, 'main/pages/post-details.html', {'post': Post.objects.get(id=pk)})


# Category  pages
class LifestyleView(ListView):
    model = Post
    template_name = 'main/categories/lifestyle.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        lifestyle = Category.objects.get(id=1)
        queryset = lifestyle.post_set.all()
        return  queryset

# def lifestyle(request):
#     lifestyle = Category.objects.get(id=1)
#     post = lifestyle.post_set.all()
#     return render(request, 'main/categories/lifestyle.html', {'post': post})



class NatureView(ListView):
    model = Post
    template_name = 'main/categories/nature.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        nature = Category.objects.get(id=2)
        queryset = nature.post_set.all()
        return  queryset


# def nature(request):
#     nature = Category.objects.get(id=2)
#     post = nature.post_set.all()
#     return render(request, 'main/categories/nature.html', {'post': post})



class CreativeView(ListView):
    model = Post
    template_name = 'main/categories/creative.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        creative = Category.objects.get(id=3)
        queryset = creative.post_set.all()
        return  queryset


# def creative(request):
#     creative = Category.objects.get(id=3)
#     post = creative.post_set.all()
#     return render(request, 'main/categories/creative.html', {'post': post})


class MotivationView(ListView):
    model = Post
    template_name = 'main/categories/motivation.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        motivation = Category.objects.get(id=4)
        queryset = motivation.post_set.all()
        return  queryset

# def motivation(request):
#     motivation = Category.objects.get(id=4)
#     post = motivation.post_set.all()
#     return render(request, 'main/categories/motivation.html', {'post': post})


class InspirationView(ListView):
    model = Post
    template_name = 'main/categories/inspiration.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        inspiration = Category.objects.get(id=5)
        queryset = inspiration.post_set.all()
        return  queryset

# def inspiration(request):
#     inspiration = Category.objects.get(id=5)
#     post = inspiration.post_set.all()
#     return render(request, 'main/categories/inspiration.html', {'post': post})



class TravelView(ListView):
    model = Post
    template_name = 'main/categories/travel.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        travel = Category.objects.get(id=5)
        queryset = travel.post_set.all()
        return  queryset


# def travel(request):
#     travel = Category.objects.get(id=6)
#     post = travel.post_set.all()
#     return render(request, 'main/categories/travel.html', {'post': post})


# Authentication
def register(request):
    return render(request, 'main/pages/registr.html')


def login(request):
    return render(request, 'main/pages/signin.html')


def gotopage(request):
    page = request.GET['page']
    return redirect('/?page='+page)    
