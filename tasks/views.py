from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def index(request):
    # This is pulling all of the tasks from the database 
    tasks = Task.objects.all()
    # This seems to be assigning them to a key 
    context = {'tasks' :tasks}
    # This is then rendering the tasks into the HTML template for loop
    return render(request, 'tasks/list.html', context)
