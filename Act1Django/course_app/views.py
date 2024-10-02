from django.shortcuts import render

def index(request):
    return render(request, 'course/index.html')

def details(request):
    return render(request, 'course/details.html')

def enroll(request):
    return render(request, 'course/enroll.html')
