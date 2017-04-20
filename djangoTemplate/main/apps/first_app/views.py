from django.shortcuts import render, redirect
# from .models import <name>


def index(request):
	return render(request, "first_app/index.html")
