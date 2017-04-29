from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index(request): 
	return render(request, "first_app/index.html")

def process(request, route):
	if request.method == "POST":
		# this brings in the value of response_to_views
		if route == "register":
			response_from_models = User.objects.validateUser(request.POST)
		elif route == "login":
			response_from_models = User.objects.loginUser(request.POST)
		if not response_from_models["status"]:
			for error in response_from_models["errorStr"]:
				messages.error(request, error)
			return redirect("login:index")
	request.session["user_id"] = response_from_models["userobj"].id
	return redirect("content:mainpage")

def logout(request):
	request.session.flush()
	return redirect("login:index")