from django.shortcuts import render

def index(request):
    return render(request, "first_app/index.html")

def projects(request):
    return render(request, "first_app/projects.html")

def aboutus(request):
    return render(request, "first_app/aboutus.html")

def testimonials(request):
    return render(request, "first_app/testimonials.html")