from django.shortcuts import render, redirect
from ..first_app.models import User


def main(request):
	if not request.session["user_id"]:
		return redirect("login:logout")
	context = {
		"this_user" : User.objects.get(id=request.session["user_id"])
	}
	return render(request, "content_app/main.html", context)
