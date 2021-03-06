from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
        form=UserRegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('blog-home')
            
    return render(request,'users/register.html',{'form':form})