from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the work05 index.")

from django.shortcuts import render

def top(request):
    return render(request, 'work05/top.html')  # templates/work05/top.html を表示

def index(request):
    return render(request, 'work05/index.html')

def list(request):
    return render(request, 'work05/list.html')
