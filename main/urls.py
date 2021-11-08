from django.urls import path
from .views import *


urlpatterns = [
    # Main page
    path('', home, name='home'),
    path('blog/', blog, name='blog-page'),

    # Authentication
    path('register/', register, name='registr'),
    path('login/', login, name="signin"),

    # Category Pages
    path('lifestyle/', lifestyle, name="lifestyle"),
    path('nature/', nature, name="nature"),
    path('creative/', creative, name="creative"),
    path('motivation/', motivation, name="motivation"),
    path('inspiration/', inspiration, name="inspiration"),
    path('travel/', travel, name="travel"),
 
]