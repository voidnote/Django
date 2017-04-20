from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
      "courses": Course.objects.all()
  } 
    return render(request, "first_app/index.html", context)

def process(request):
  Course.objects.create(name=request.POST['name'], description=request.POST['description'])
  return redirect("/")

def remove(request, id):
  course = Course.objects.get(id=id)
  print course
  print course.name
  context = {
      "course_id": course
  } 
  return render(request, "first_app/destroy.html", context)

def kill(request, id):
  Course.objects.filter(id=id).delete()
  return redirect("/")