from django.urls import path
from . import views
from .views import login1,register1
app_name = 'shouye'

urlpatterns = [
#    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login1/',login1.as_view(), name='login1'),
    path('register1/', register1.as_view(), name='register1'),
]