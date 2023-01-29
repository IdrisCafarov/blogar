from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('category_detail/<slug>/',category_detail,name="category_detail"),
    path('blog_detail/<slug>/',blog_detail,name="blog_detail"),
    path('about',about,name="about"),
    
]