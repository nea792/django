from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    return render(request,'users/main.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            form=UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,f' sign up successfully {form.cleaned_data["username"]} ')
                return redirect('login')

        else:
            form=UserRegisterForm()
        context={
            'form':form
        }
        return render(request,'users/register.html',context)

@login_required()
def profile(request):
    if request.method=="POST":
            u_form=UserUpdateForm(request.POST,instance=request.user)
            p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
            'u_form':u_form,
            'p_form':p_form,
        }
    return render(request,'users/profile.html',context)