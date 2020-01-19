from django.urls import path
from . import views
from .views import swgslist,swgsdetails,swsjlist,swsjdetails
app_name = 'siwang'

urlpatterns = [
    #path('index/', views.index, name='index'),
    path('swgslist/', swgslist.as_view(), name='swgslist'),
    path('swgsdetails/', swgsdetails.as_view(), name='swgsdetails'),
    path('swsjlist/', swsjlist.as_view(), name='swsjlist'),
    path('swsjdetails/', swsjdetails.as_view(), name='swsjdetails'),
]