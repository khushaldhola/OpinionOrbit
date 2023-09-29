from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': "Let's learn Bharatiya history"},
    {'id': 2, 'name': "Data Science with sklearn"},
    {'id': 3, 'name': "why colleges not worth it"},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')