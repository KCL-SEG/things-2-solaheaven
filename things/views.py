from django.shortcuts import render

from .forms import ThingForm


def home(request):
    return render(request, 'home.html')


def thing_form(request):
    form = ThingForm()
    return render(request, 'thing_form.html', {'form':form})