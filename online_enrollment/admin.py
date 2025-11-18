from django.contrib import admin
from .models import TestingDatabase, Students, Course, Enrollment, Subjects, Instructor
# Register your models here.
admin.site.register(TestingDatabase)
admin.site.register(Students)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Subjects)
admin.site.register(Instructor)