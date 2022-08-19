from unicodedata import digit
from django.shortcuts import render,redirect
from num2words import num2words
# Create your views here.
def index(request):
    if request.method=='POST':
        num=request.POST['number']
        finalnum=num2words(num)        
        return render(request,'base.html',{'finalnum':finalnum})
    else:
        return render(request,'base.html')