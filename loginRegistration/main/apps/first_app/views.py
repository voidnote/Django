from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index(request): 
	return render(request, "first_app/index.html")

def process(request, route):
	if request.method == "POST":
		# this brings in the value of response_to_views
		if route == "register":
			response_from_models = User.object.validateUser(request.POST)
		else:
			response_from_models = User.object.loginUser(request.POST)
		if not response_from_models["status"]:
			for error in response_from_models["errors"]:
				messages.error(request, error)
			return redirect("/")
	return redirect("/success/"+str(response_from_models["userobj"].id)+"/"+route)

def success(request, id, route): 
	context = {
		"user" : User.object.get(id=id),
		"route" : route
	}
	return render(request, "first_app/success.html", context)