from django.shortcuts import render, redirect
from .models import Book

def index(request):
    context = {
      "books": Book.objects.all()
  } 
    return render(request, "first_app/index.html", context)

def process(request):
  Book.objects.create(title=request.POST['title'], category=request.POST['category'], author=request.POST['author'])
  return redirect("/")