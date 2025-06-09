from django.shortcuts import render

# Create your views here.
# display_info/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'display_info/index.html')
