from django.urls import path
from .views import cygslist,cygsdetails,cysjlist,cysjdetails,cyzlist,cyzdetails

app_name = 'chuangye'

urlpatterns = [
#    path('', TemplateView.as_view(template_name='index.html'), name='index'),
#    path('cyindex/', cyindex.as_view(), name='cyindex'),
    path('cygslist/', cygslist.as_view(), name='cygslist'),
    path('cygsdetails/', cygsdetails.as_view(), name='cygsdetails'),
    path('cysjlist/', cysjlist.as_view(), name='cysjlist'),
    path('cysjdetails/', cysjdetails.as_view(), name='cysjdetails'),
    path('cyzlist/', cyzlist.as_view(), name='cyzlist'),
    path('cyzdetails/', cyzdetails.as_view(), name='cyzdetails'),
]