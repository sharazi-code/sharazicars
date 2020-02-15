from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='cars'),
    path('post/<slug:pk>',views.Post,name='sharazi'),
    path("blog",views.Blog,name='blog'),
    path("companyname",views.Brandname,name='brandname'),
    path('car/<slug:pk>',views.Cardetails,name='cardetails'),
    path("policy",views.Policy,name='policy'),
    path("about",views.About,name='about'),
    path("disclaimer",views.Disclaimer,name='disclaimer'),
    path("videos",views.Videos,name='videos'),
]