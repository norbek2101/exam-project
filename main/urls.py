from django.urls import path
from .views import *


urlpatterns = [
    # Main page
    path('', home, name='home'),
    # path('blog/', blog, name='blog-page'),
    path('blog/', BlogListView.as_view(), name='blog-page'),
    path('post_detail/<int:pk>/', post_detail, name='post-detail'),

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


    # path('lifestyle/', lifestyle, name="lifestyle"),
    # path('nature/', nature, name="nature"),
    # path('creative/', creative, name="creative"),
    # path('motivation/', motivation, name="motivation"),
    # path('inspiration/', inspiration, name="inspiration"),
    # path('travel/', travel, name="travel"),


    path('gotopage/', gotopage, name='gotopage')
 
]