from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Index.html')
def about(request):
    return render(request, 'About.html')
def login(request):
    return render(request, 'Login.html')