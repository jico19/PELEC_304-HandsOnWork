import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enrollment.settings")
django.setup()

from online_enrollment.models import Subjects

from datetime import time

subjects = [
    ("MATH101", "Calculus I", "Lecture", "Room 101", "Math", time(8, 0)),
    ("ENG102", "English Lit", "Lecture", "Room 102", "English", time(9, 30)),
    ("CS103", "Intro to CS", "Lab", "Lab 1", "CS", time(11, 0)),
    ("HIST104", "World History", "Lecture", "Room 103", "History", time(13, 0)),
    ("PHYS105", "Physics I", "Lecture", "Room 104", "Physics", time(14, 30)),
    ("CHEM106", "Chemistry I", "Lab", "Lab 2", "Chemistry", time(8, 0)),
    ("BIO107", "Biology I", "Lecture", "Room 105", "Biology", time(9, 30)),
    ("ECON108", "Economics", "Lecture", "Room 106", "Economics", time(11, 0)),
    ("PSY109", "Psychology", "Lecture", "Room 107", "Psychology", time(13, 0)),
    ("ART110", "Art Appreciation", "Lecture", "Room 108", "Arts", time(14, 30)),
]

for s in subjects:
    Subjects.objects.create(
        subject_code=s[0],
        subject_name=s[1],
        instruction=s[2],
        room=s[3],
        department=s[4],
        time=s[5]  # single time object
    )

print("10 subjects added successfully!")
