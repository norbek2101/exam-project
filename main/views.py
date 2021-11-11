from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Post, Tag
from django.views.generic import  ListView, CreateView, DetailView
from .forms import *
from django.contrib import messages
from django.contrib import auth
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.db.models import Count


# Main page
def home(request):
    tags = Tag.objects.all()
    context={'tags':tags}
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/pages/about.html')    

 
class BlogListView(ListView):
    model = Post
    template_name = 'main/pages/blog.html' 
    context_object_name = 'post'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] =  Tag.objects.all()
        return context

    # def get_queryset(self):
    #     return Post.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')    

# class PostDetailView(DetailView):
#     model = Post
#     form = CommentForm
#     template_name = 'main/pages/post-details.html'

#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             post = self.get_object()
#             form.instance.author = request.user
#             form.instance.post = post
#             form.save()
#             return redirect('post-detail', post.pk)


#     def get_context_data(self, **kwargs):
#         post_comments = self.get_object().comment_set.all()
#         context = super().get_context_data(**kwargs)
#         context['tags'] = self.get_object().tags.all()
#         context['form'] = self.form
#         context['post_comments'] = post_comments
#         return context 


     

def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('post-detail', pk)


def dislike_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.dislikes.add(request.user)
    return redirect('post-detail', pk)          


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    tags = post.tags.all()
    post_comments = post.comment_set.all()
    num_comments = post_comments.count()
    form = CommentForm()
    views = Post.objects.filter(pk=pk).update(views=F('views') + 1)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = post
            form.instance.author = request.user
            form.instance.post = post
            form.save()
            return redirect('post-detail', post.pk)
    
    context = {'views':views, 'form':form, 'post':post, 'tags':tags, 'post_comments':post_comments, 'num_comments':num_comments}
    return render(request,'main/pages/post-details.html', context)


class PostCreateView(CreateView):
    model = Post
    fields = ['category', 'title', 'content', 'tags', 'image']
    template_name='main/pages/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('signin')

    context = {'form': form}
    return render(request, 'main/pages/registr.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('blog-page')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'main/pages/signin.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('signin')    

def gotopage(request):
    page = request.GET['page']
    return redirect('/?page='+page)   



    
