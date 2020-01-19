from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class cygslist(View):

    def get(self, request):
        return render(request, 'chuangye/cygslist.html')

class cygsdetails(View):

    def get(self, request):
        return render(request, 'chuangye/cygsdetails.html')

class cysjlist(View):

    def get(self, request):
        return render(request, 'chuangye/cysjlist.html')

class cysjdetails(View):

    def get(self, request):
        return render(request, 'chuangye/cysjdetails.html')

class cyzlist(View):

    def get(self, request):
        return render(request, 'chuangye/cyzlist.html')

class cyzdetails(View):

    def get(self, request):
        return render(request, 'chuangye/cyzdetails.html')


# Create your views here.
