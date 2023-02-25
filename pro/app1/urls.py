from django.urls import path
from . import views


urlpatterns = [
    path('home' , views.home , name="Home"),
    path('base' , views.base , name="Base"),
    
]
