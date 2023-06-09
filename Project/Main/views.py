from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "Main/index.html")

def toNavigation(request):
    return render(request, "Navigation/index.html")

def toImageGallery(request):
    return render(request, "Image_Gallery/index.html")

def toLayout(request):
    return render(request, "Layout/index.html")