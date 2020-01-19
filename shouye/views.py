from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
class login1(View):
    def login1(request):
        return render(request,'shouye/login.html')

class register1(View):
    def register1(request):
        return render(request,'shouye/register.html')

# Create your views here.
