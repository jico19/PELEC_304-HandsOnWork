from django.shortcuts import render, HttpResponse

# Create your views here.
def register(req):
    return HttpResponse("This is register View.")

def register_user(req):
    return HttpResponse("user registered")
