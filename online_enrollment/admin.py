from django.contrib import admin
from .models import Students, Course, Enrollment, Subjects, Instructor
# Register your models here.
admin.site.register(Students)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Subjects)
admin.site.register(Instructor)