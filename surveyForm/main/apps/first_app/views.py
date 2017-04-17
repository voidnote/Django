from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if "submission" not in request.session:
        request.session["submission"] = 0
    else:
        request.session["submission"] += 1    
    return render(request, "first_app/index.html")

def process(request):
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comment"] = request.POST["comment"]
    return redirect('/result')

def result(request):
    return render(request, "first_app/result.html")