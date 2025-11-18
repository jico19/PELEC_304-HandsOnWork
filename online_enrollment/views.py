from django.shortcuts import render, get_object_or_404, redirect
from .models import Students, Subjects, Instructor, Enrollment, Course
from .forms import StudentForm, SubjectsForm, RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def StudentView(request):
    students_data = Students.objects.all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()

    return render(request, 'apps/students.html', {
        "students": students_data,
        "forms": form
    })

def UpdateStudentView(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'apps/update_student.html', {
        "forms": form
    })

def DeleteStudentView(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        if student:
            student.delete()
            return redirect('students')

    return render(request, 'apps/student_delete_conf.html')

def SubjectsView(request):
    subjects_data = Subjects.objects.all()

    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubjectsForm()

    return render(request, 'apps/subjects.html', {
        "subjects": subjects_data,
        "forms": form
    })

def UpdateSubjectsView(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)
    if request.method == 'POST':
        form = SubjectsForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectsForm(instance=subject)

    return render(request, 'apps/update_subject.html', {
        "forms": form
    })

def DeleteSubjectView(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)
    if request.method == 'POST':
        if subject:
            subject.delete()
            return redirect('subjects')
        
    return render(request, 'apps/subject_delete_conf.html')

def HomeView(request):
    # redirect user if not login
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'apps/home.html')


def LoginView(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                print("dasds")
                return redirect('home')
            else:
                messages.error(request, "You have entered a invalid credentials")
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'apps/login.html', {
        "forms": form
    })


def RegisterView(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            messages.success(request, "Successfully registerd. please proceed to login.")
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'apps/register.html', {
        "forms": form
    })

def LogoutView(request):
    logout(request)
    return redirect('login')