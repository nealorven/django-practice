from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    context = {'name': 'Neal'}
    return render(request, 'home.html', context)
