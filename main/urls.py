from django.urls import path
from .views import *


urlpatterns = [
    # Main page
    path('', home, name='home'),
    path('blog/', BlogListView.as_view(), name='blog-page'),
    path('post_detail/<int:pk>/',  post_detail, name='post-detail'),
    # path('post_detail/<int:pk>/',  PostDetailView.as_view(), name='post-detail'),
    path('like/<int:pk>/', like_post, name="like_post"),
    path('dislike/<int:pk>/', dislike_post, name="dislike_post"),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', about, name='about'),
    # path('profile/', profile, name='profile'),


    # Authentication
    path('register/', register, name='registr'),
    path('login/', login, name="signin"),
    path('logout/', logout, name='logout'),

    # Category Pages
    path('lifestyle/', LifestyleView.as_view(), name='lifestyle'),
    path('nature/', NatureView.as_view(), name='nature'),
    path('creative/', CreativeView.as_view(), name='creative'),
    path('motivation/', MotivationView.as_view(), name='motivation'),
    path('inspiration/', InspirationView.as_view(), name='inspiration'),
    path('travel/', TravelView.as_view(), name='travel'),
 
    path('gotopage/', gotopage, name='gotopage')
 
]