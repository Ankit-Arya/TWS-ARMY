from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def LearnPage(request):
    return render(request, 'LearnPage.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
