from django.shortcuts import render, redirect
from django.http import HttpResponse

from tasks.forms import TaskForm

# Create your views here.
from .models import *

def index(request):
    # This is pulling all of the tasks from the database 
    tasks = Task.objects.all()
    # This seems to be assigning them to a key 
    form =  TaskForm()
   

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks,'form':form}
    # This is then rendering the tasks into the HTML template for loop
    return render(request, 'tasks/list.html', context)
