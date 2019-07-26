from django.shortcuts import render
from django.http import HttpResponse
from .models import first

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name = "index/home.html",
                  context = {"first" : first.objects.all})