from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# class tzindex(View):
#
#     def get(self, request):
#         return render(request, 'touzi/tzindex.html')

class tzjglist(View):

    def get(self, request):
        return render(request, 'touzi/tzjglist.html')

class tzjgdetails(View):

    def get(self, request):
        return render(request, 'touzi/tzjgdetails.html')

class tzsjlist(View):

    def get(self, request):
        return render(request, 'touzi/tzsjlist.html')

class tzsjdetails(View):

    def get(self, request):
        return render(request, 'touzi/tzsjdetails.html')

class tzzlist(View):

    def get(self, request):
        return render(request, 'touzi/tzzlist.html')

class tzzdetails(View):

    def get(self, request):
        return render(request, 'touzi/tzzdetails.html')


# Create your views here.
