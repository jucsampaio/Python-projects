from django.contrib import admin
from django.urls import path
from libray.views import index, about, contact, post, morteintern


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', index),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('post', post, name='post'),
    path('morteintern', morteintern, name='morteintern')
   
    ]


               
    
    
    
    
    
    
   
   

