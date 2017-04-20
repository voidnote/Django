from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages


def index(request): 
	return render(request, "first_app/index.html")

def process(request):
	if request.method == "POST":
		# this brings in the value of response_to_views
		response_from_models = Users.run.validateUser(request.POST)
		if not response_from_models["status"]:
			for error in response_from_models["errors"]:
				messages.error(request, error)
		else:
			print response_from_models["userobj"]
	return redirect("/results")

def results(request): 
	context = {
		"users" : Users.run.all()
	}
	return render(request, "first_app/results.html", context)