from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():     
            form.save()   
            return redirect(reverse('Home'))
        else:
            print('Form invalid')
            print(form.errors)
            context =  {'form':form,} 
            return render (request,'register.html',context)
    form = NewUserForm()   #if the data is not valid then reset the form to its default
    context =  {'form':form,} 
    
    return render (request,'register.html',context)    


def logout_view(request):
    logout(request)
    return redirect('logout.html') 