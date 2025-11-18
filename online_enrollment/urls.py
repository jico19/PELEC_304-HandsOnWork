from django.urls import path
from . import views



urlpatterns = [
    # atuh register 
    path('', views.LoginView, name="login"),
    path('register/', views.RegisterView, name="register"),
    path('logout/', views.LogoutView, name="logout"),
    # pages
    path('home/', views.HomeView, name="home"),
    # students
    path('students/', views.StudentView, name="students"),
    path('students/update/<int:pk>/', views.UpdateStudentView, name="update_student"),
    path('students/delete/<int:pk>/', views.DeleteStudentView, name="delete_student"),
    # subjects
    path('subjects/', views.SubjectsView, name="subjects"),
    path('subjects/update/<int:pk>/', views.UpdateSubjectsView, name="update_subject"),
    path('subjects/delete/<int:pk>/', views.DeleteSubjectView, name="delete_subject"),

]
