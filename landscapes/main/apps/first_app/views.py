from django.shortcuts import render

def index(request):
    return render(request, "first_app/index.html")

def scenery(request, value):
    val = int(value)
    context = {
        "imgID" : val
    }
    return render(request, "first_app/scenery.html", context)

