from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def index(request):
    '3D POI Site'
    return render_to_response('POI3D/index.html', {})
