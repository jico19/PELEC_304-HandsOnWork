from django.shortcuts import render, HttpResponse

# Create your views here.
def view_students(req):
    return HttpResponse("This is student View.")

def add_student(req):
    return HttpResponse("student added!")

def delete_student(req, id):
    return HttpResponse('delete student!')