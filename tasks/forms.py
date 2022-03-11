from asyncio import tasks
from multiprocessing import context
from tkinter.tix import Form
from urllib import request
from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields =  '__all__'
        
