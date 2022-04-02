from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('contact',views.contact, name='contact'),
    path('learn/<str:slug>',views.learn, name='learn'),
    path('courses',views.courcesP, name='moreCources'),
    path('search',views.search, name='search'),
    path('about',views.aboutus, name='about'),
]