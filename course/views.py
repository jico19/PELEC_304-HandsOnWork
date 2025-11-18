from django.shortcuts import render, HttpResponse

# Create your views here.
def course_view(req):
    return HttpResponse("This is course View.")

def add_course(req):
    return HttpResponse("hello world")

def delete_course(req,id):
    return HttpResponse(f"Delete Course View: id {id}")