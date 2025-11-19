from django import forms
from .models import Students, Course, Enrollment, Subjects, Instructor
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = ['user']
        

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email']  # You forgot email here

    def clean(self):
        data = super().clean()

        p1 = data.get('password1')
        p2 = data.get('password2')

        if p1 and len(p1) < 8:
            raise forms.ValidationError("Password cannot be shorter than 8 characters.")

        if p1 != p2:
            raise forms.ValidationError("Passwords do not match.")

        return data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
