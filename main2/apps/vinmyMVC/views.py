from django.shortcuts import render, redirect
import datetime, math, random
import urllib2

# Create your views here.
def index(request):
    request.session['value'] = 'The Simpsons'
    request.session['counter'] = 0
    context = {
    "site_visits" : request.session['counter'] 
    }
    return render(request, 'vinmyMVC/index.html', context)

def show(request):
    print(request.method)
    return render(request, 'vinmyMVC/show_users.html')

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.method
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

def time(request):
    context = {
    "date":"{:%Y-%m-%d}".format(datetime.date.today()),
    "time":"{:%H:%M:%S}".format(datetime.datetime.now())
    }
    return render(request, 'vinmyMVC/index.html', context)

def randomword(request):
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib2.urlopen(word_site)
    txt = response.read()
    WORDS = txt.splitlines()
    randomnum = random.randint(0,25487)
    request.session['counter'] += 1    
    context = {
    "randomword" : WORDS[randomnum],
    "site_visits" : request.session['counter'] 
    }
    return render(request, 'vinmyMVC/index.html', context)