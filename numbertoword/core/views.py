from django.shortcuts import render
from .utils import numset
# Create your views here.
def index(request):
    
    return render(request,'base.html')