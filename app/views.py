from django.shortcuts import render

# Create your views here.
def one(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'one.html',d)
