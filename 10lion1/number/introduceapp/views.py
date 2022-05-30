from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home.html')
def subject(request):
    return render(request, 's.html')
def bootstrap(request):
    return render(request, 'bootstrap.html')