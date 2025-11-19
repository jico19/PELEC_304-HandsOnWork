from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} - {self.section}"

class Subjects(models.Model):
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    instruction = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    time = models.TimeField()  # make sure this exists


    def __str__(self):
        return f"{self.subject_code} - {self.subject_name} - {self.time.strftime('%I:%M %p')}"


class Instructor(models.Model):
    instructor_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.instructor_id} - {self.last_name} - {self.department}"
    
class Enrollment(models.Model):
    student_id = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    section = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} - {self.course}"

class Course(models.Model):
    course_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=200)
    course_description = models.CharField(max_length=200)
    students_enrolled = models.IntegerField()
    program_head = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_name} - {self.program_head}"
