from django.shortcuts import render
from django.views.generic import ListView

from .models import Picture

def index(request):
    index= Picture.objects.all()
    return render (request,'index.html',{'index' : index})