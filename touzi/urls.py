from django.urls import path
from . import views
from .views import tzjglist,tzjgdetails,tzsjlist,tzsjdetails,tzzlist,tzzdetails
app_name = 'touzi'

urlpatterns = [
    path('tzjglist/', tzjglist.as_view(), name='tzjglist'),
    path('tzjgdetails/', tzjgdetails.as_view(), name='tzjgdetails'),
    path('tzsjlist/', tzsjlist.as_view(), name='tzsjlist'),
    path('tzsjdetails/', tzsjdetails.as_view(), name='tzsjdetails'),
    path('tzzlist/', tzzlist.as_view(), name='cyzlist'),
    path('tzzdetails/', tzzdetails.as_view(), name='tzzdetails'),
]
