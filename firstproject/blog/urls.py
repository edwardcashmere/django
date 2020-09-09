from django.urls import path
from .views import home,about


urlpatterns=[
    path('',home, name='bog-home'),
    path('about/',about, name='blog-about')
    
]