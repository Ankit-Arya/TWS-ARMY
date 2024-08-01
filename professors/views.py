from django.shortcuts import render

# Create your views here.
def professorsui(request):
    return render(request, 'professors.html')