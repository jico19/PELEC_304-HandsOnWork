from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.view_students, name="students_view"),
    path('add/students/', views.add_student, name="add_student"),
    path('delete/students/<int:id>/', views.delete_student, name="delete_student")
]