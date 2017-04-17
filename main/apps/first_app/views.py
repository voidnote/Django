# CONTROLLER

from django.shortcuts import render, HttpResponse
  # the index function is called when root is visited
# def index(request):
#     response = "Hello, I am your first request!"
#     return HttpResponse(response)

def index(request):
    print ("*"*100)
    return render(request, "first_app/index.html")
