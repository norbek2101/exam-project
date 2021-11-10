from django.urls import path
from .views import *


urlpatterns = [
    # Main page
    path('', home, name='home'),
    path('blog/', BlogListView.as_view(), name='blog-page'),
    path('post_detail/<int:pk>/',  post_detail, name='post-detail'),

    # Authentication
    path('register/', register, name='registr'),
    path('login/', login, name="signin"),

    # Category Pages
    path('lifestyle/', LifestyleView.as_view(), name='lifestyle'),
    path('nature/', NatureView.as_view(), name='nature'),
    path('creative/', CreativeView.as_view(), name='creative'),
    path('motivation/', MotivationView.as_view(), name='motivation'),
    path('inspiration/', InspirationView.as_view(), name='inspiration'),
    path('travel/', TravelView.as_view(), name='travel'),
 
    path('gotopage/', gotopage, name='gotopage')
 
]