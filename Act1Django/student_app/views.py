from django.shortcuts import render

def index(request):
    return render(request, 'student/index.html')

def about(request):
    return render(request, 'student/about.html')

def contact(request):
    return render(request, 'student/contact.html')

