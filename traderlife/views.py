from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# The homepage of the whole site.
def home(request):
    return render(request,'homepage.html')

# Index of app 'traderlife'
def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, "traderlife/index.html", {"is_login": True})
    else:
        # Do something for anonymous users.
        return render(request, "traderlife/index.html", {"is_login": False})

