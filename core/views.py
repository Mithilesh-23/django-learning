from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Student, Teacher

from . forms import StudentForm, TeacherForm

def home(request):
    context = {
        "name" : "Mithil",
        "course" : "Django"
    }
    return render(request, "core/home.html", context)

def about(request):
    context = {
        "name" : "Montya",
        "course" : "AIML",
        "dept" : "CSE"
    }
    return render(request, "core/about.html", context)

def contact(request):
    context = {
        "emergency" : "100",
        "phone_no" : "1234567890",
        "email" : "e@gmail.com"
    }
    return render(request, "core/contact.html", context)

def services(request):
    context = {
        "name" : "Mithilesh"
    }
    return render(request, "core/services.html", context)

def team(request):
    context = {
        "Senior_Developer" : "Gaurav",
        "Jr_Developer" : "Mithilesh"
    }
    return render(request, "core/team.html", context)

def help(request):
    return HttpResponse("Help button 24/7")



#######     Manual Way          \#####
# # Student view 
# def student_form(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         branch = request.POST.get("branch")
#         email = request.POST.get("email")

#         Student.objects.create(
#             name = name,
#             age = age,
#             branch = branch,
#             email = email
#         )

#         return redirect("student_form")

#     return render(request, "core/student_form.html")

def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_form")
    else:
        form = StudentForm()

    return render(request, "core/student_form.html", {"form":form})

# def teacher_form(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         subject = request.POST.get("subject")
#         salary = request.POST.get("salary")
#         email = request.POST.get("email")

#         Teacher.objects.create(
#             name = name,
#             subject = subject,
#             salary = salary,
#             email = email
#         )

#         return redirect("teacher_form")

#     return render(request, "core/teacher_form.html")

def teacher_form(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("teacher_form")
    else:
        form = TeacherForm()

    return render(request, "core/teacher_form.html", {"form":form})

def student_list(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }

    return render(request, "core/student_list.html", context)

def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {
        "teachers" : teachers
    }

    return render(request, "core/teacher_list.html", context)

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")

def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect("teacher_list")