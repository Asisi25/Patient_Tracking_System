from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'theme/index.html')

def blog_details(request):
    return render(request, 'theme/blog-details.html')

def index2(request):
    return render(request, 'theme/index-2.html')
