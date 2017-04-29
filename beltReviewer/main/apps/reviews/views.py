from django.shortcuts import render, redirect
from .models import Book, Review
from django.contrib import messages

# Create your views here.
def index(request): 
	return render(request, "reviews/mainpage.html")

def add_review(request): 
	return render(request, "reviews/add_review.html")

def create_review(request): 
	if request.method == "POST":
		response_from_book_models = Book.objects.createBook(request.POST)
		response_from_review_models = Review.objects.createReview(request.POST, request.session["user_id"])
		newErrorStr = []
		if not response_from_book_models["status"]:
			for error in response_from_book_models["errorStr"]:
				newErrorStr.append(error)
		if not response_from_review_models["status"]:
			for error in response_from_review_models["errorStr"]:
				newErrorStr.append(error)		
		if newErrorStr:
			for error in newErrorStr:
				messages.error(request, error)		
			return redirect("reviews:add_reviews")
	return redirect("reviews:show_review")

def show_review(request): 
	context = {
		"all_reviews": Review.objects.all()
	}

	
	return render(request, "reviews/show_review.html", context)