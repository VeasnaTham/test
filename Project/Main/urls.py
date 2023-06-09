from django.urls import path
from . import views

app_name = "Main"
urlpatterns = [
    path("", views.index, name="index"),
    path("Navigation/", views.toNavigation, name="Navigation"),
    path("ImageGallery/", views.toImageGallery, name="ImageGallery"),
    path("Layout/", views.toLayout, name="Layout"),

]
