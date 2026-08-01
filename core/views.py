from django.http import HttpResponse
from django.shortcuts import render

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
