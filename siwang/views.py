from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class swgslist(View):

    def get(self, request):
        return render(request, 'siwang/swgslist.html')

class swgsdetails(View):

    def get(self, request):
        return render(request, 'siwang/swgsdetails.html')

class swsjlist(View):

    def get(self, request):
        return render(request, 'siwang/swsjlist.html')

class swsjdetails(View):

    def get(self, request):
        return render(request, 'siwang/swsjdetails.html')

# Create your views here.
