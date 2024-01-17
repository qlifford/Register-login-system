from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.
class Home(ListView):
    model = Article

def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
            return redirect('home')
    return render(request, 'registration/reg.html', {'form': RegForm})
