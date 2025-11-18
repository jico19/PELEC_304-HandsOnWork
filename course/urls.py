from django.urls import path
from . import views

urlpatterns = [
    path('add/course/', views.add_course, name="create_course"),
    path('courses/', views.course_view, name="view_course"),
    path('delete/course/<int:id>/', views.delete_course, name="delete_course")
]