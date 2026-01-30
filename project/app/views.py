from django.shortcuts import render

# Create your views here.
def select(req):
    return render(req,'select.html')
def select1(req):
    print("hello")
    print(req.method)
    print(req.GET)
    x=req.GET.get('selectedoption')
    print(x)
