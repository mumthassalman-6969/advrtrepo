from django.shortcuts import render

# Create your views here. 
def fnadd(req):
    return render(req,'home.html')