from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("team/", views.team, name="team"),
    path("help/", views.help, name="help"),

    path("student-form/", views.student_form, name="student_form"),
    path("teacher-form/", views.teacher_form, name ="teacher_form"),
    
    
]