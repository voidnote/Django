from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def ninjas(request):
    return render(request, "first_app/ninjas.html")

def color(request, color):
    context = {
        "color" : color
    }
    return render(request, "first_app/color.html", context)