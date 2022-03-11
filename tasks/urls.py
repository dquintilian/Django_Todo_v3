from django.urls import path 
from . import views

urlpatterns = [
    # This is telling the index of the website to load in the views here I think?
    path('', views.index)
]