from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Website home page
def index(request):
    # return HttpResponse("Hello, world. You're at our website home page.")
    return render(request, "website/index.html")