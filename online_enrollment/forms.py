from django import forms
from .models import TestingDatabase, Students, Course, Enrollment, Subjects, Instructor
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        
class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'



class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput())




class RegisterForm(forms.ModelForm):

    password2 = forms.CharField(
        label="Re-Type Password:",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
    
    def clean(self):
        # validation
        clean_data = super().clean()
        
        if len(clean_data['password']) < 8:
            raise forms.ValidationError("Password cannot be shorter than 8.")
        
        if clean_data['password'] != clean_data['password2']:
            raise forms.ValidationError("Password doesnt match.")
        
        return clean_data