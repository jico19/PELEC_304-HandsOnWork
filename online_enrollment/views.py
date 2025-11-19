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

    return render(request, 'student/students.html', {
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

    return render(request, 'student/update_student.html', {
        "forms": form
    })

def DeleteStudentView(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        if student:
            student.delete()
            return redirect('students')

    return render(request, 'student/student_delete_conf.html')

def SubjectsView(request):
    subjects_data = Subjects.objects.all()

    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        print(form)
        if form.is_valid():
            print("tite")
            form.save()
    else:
        form = SubjectsForm()

    return render(request, 'subjects/subjects.html', {
        "subjects": subjects_data,
        "form": form
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

    return render(request, 'subjects/update_subject.html', {
        "forms": form
    })

def DeleteSubjectView(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)
    if request.method == 'POST':
        if subject:
            subject.delete()
            return redirect('subjects')
        
    return render(request, 'subjects/subject_delete_conf.html')

def HomeView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'common/home.html')

def ProfileView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    # checks if user has a students profile
    try:
        user_profile_data = Students.objects.get(user__pk=pk)
        subjects = Subjects.objects.all()
        
    except Students.DoesNotExist:
        user_profile_data = None
    
    
    return render(request, 'common/profile.html', {
        "user_data": user_profile_data,
        "subjects": subjects
    })

def ConfigureProfileView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user  # attach logged-in user here
            student.save()
            return redirect('profile', pk=student.pk)
        else:
            print(form.errors)  # debug any other errors
    else:
        form = StudentForm()

    return render(request, 'common/config_profile.html', {
        "form": form,
        
    })


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

    return render(request, 'auth/login.html', {
        "forms": form
    })

def RegisterView(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data['username'],
                password=data['password1']
            )
            messages.success(request, "Successfully registerd. please proceed to login.")
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {
        "forms": form
    })

def LogoutView(request):
    logout(request)
    return redirect('login')