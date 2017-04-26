from django.shortcuts import render, redirect
from .models import User, Secret
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
			for error in response_from_models["errorStr"]:
				messages.error(request, error)
			return redirect("/")
	return redirect("/secrets/"+str(response_from_models["userobj"].id)+"/"+route)

def secrets(request, id, route): 
	context = {
		"user" : User.object.get(id=id),
		"route" : route,
		"secrets" : Secret.objects.all(),
	}
	return render(request, "first_app/secrets.html", context)

def post(request, id): 
	Secret.objects.create(secret = request.POST["secret"], user = User.object.get(id=id))
	route = "post"
	return redirect("/secrets/"+str(id)+"/"+route)

def like(request, userid, secretid): 
	this_user = User.object.get(id=userid)
	this_secret = Secret.objects.get(id=secretid)
	this_secret.likes.add(this_user)
	route = "like"
	return redirect("/secrets/"+str(userid)+"/"+route)

def logout(request):
	context = {}
	return redirect("/")