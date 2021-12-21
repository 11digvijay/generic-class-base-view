from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Laptop
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

class laptopcreateview(LoginRequiredMixin,CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/cbv/list/'

class laptoplistview(ListView):
    model = Laptop

class laptopupdateview(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/cbv/list/'

class laptopdeleteview(DeleteView):
    model = Laptop
    success_url = '/cbv/list/'