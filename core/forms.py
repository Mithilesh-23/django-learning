from django import forms
from .models import Student, Teacher

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = "__all__"    ##It tells Django: Create form fields for every field in the Student model.
#         widgets = {
#             "name": forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter your full name"
#             }),
#             "email": forms.EmailInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter your email"
#             }),
#             "age": forms.TextInput(attrs={
#                             "class": "form-control",
#                             "placeholder": "Enter your Age"
#             }),
#         }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"    ##It tells Django: Create form fields for every field in the Student model.
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email"
            }),
            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your Age"
            }),
        }

        labels = {
            "name" : "Student Name",
            "age" : "Student Age",
            "branch" : "Department",
            "email" : "Email Address",
        }

        help_texts = {
        "email": "Enter a valid email address.",
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name"
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your Subject"
            }),
            "salary": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your salary"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email"
            }),
        }
        
        labels = {
            "name" : "Teacher Name",
            "subject" : "Teacher Subject",
            "salary" : "Teacher Salary",
            "email" : "Teacher email"
            }
        
        help_texts = {
                "email": "Enter a valid email address.",
        }
        