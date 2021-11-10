from django.http import request
from django.shortcuts import redirect, render
from .models import Category, Post, Tag
from django.views.generic import  ListView, DetailView


# Main page
def home(request):
    return render(request, 'main/index.html')

 
class BlogListView(ListView):
    model = Post
    template_name = 'main/pages/blog.html' 
    context_object_name = 'post'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] =  Tag.objects.all()
        return context


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    tags = post.tags.all()
    context = {'post':post, 'tags':tags}
    return render(request,'main/pages/post-details.html', context)



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] =  Tag.objects.all()
        return context    

 
class NatureView(ListView):
    model = Post
    template_name = 'main/categories/nature.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        nature = Category.objects.get(id=2)
        queryset = nature.post_set.all()
        return  queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] =  Tag.objects.all()
        return context

 
class CreativeView(ListView):
    model = Post
    template_name = 'main/categories/creative.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        creative = Category.objects.get(id=3)
        queryset = creative.post_set.all()
        return  queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] =  Tag.objects.all()
        return context
 

class MotivationView(ListView):
    model = Post
    template_name = 'main/categories/motivation.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        motivation = Category.objects.get(id=4)
        queryset = motivation.post_set.all()
        return  queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] =  Tag.objects.all()
        return context    

 
class InspirationView(ListView):
    model = Post
    template_name = 'main/categories/inspiration.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        inspiration = Category.objects.get(id=5)
        queryset = inspiration.post_set.all()
        return  queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] =  Tag.objects.all()
        return context    
 

class TravelView(ListView):
    model = Post
    template_name = 'main/categories/travel.html' 
    context_object_name = 'post'
    paginate_by = 2
    
    def get_queryset(self):
        travel = Category.objects.get(id=6)
        queryset = travel.post_set.all()
        return  queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] =  Tag.objects.all()
        return context  

# Authentication
def register(request):
    return render(request, 'main/pages/registr.html')


def login(request):
    return render(request, 'main/pages/signin.html')


def gotopage(request):
    page = request.GET['page']
    return redirect('/?page='+page)    
