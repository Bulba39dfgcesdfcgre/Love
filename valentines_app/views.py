from django.shortcuts import render

def home(request):
    return render(request, 'valentines_app/home.html')

def success(request):
    return render(request, 'valentines_app/success.html')