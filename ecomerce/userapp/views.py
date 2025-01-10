from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import Profile
from .forms import ProfileForm
from django import forms




def Register(request):
    if request.method == 'POST':
        f_name=request.POST['firstname']
        l_name = request.POST['lastname']
        name=request.POST['username']
        mail = request.POST['email']
        lock1 = request.POST['password1']
        lock2 = request.POST['password2']
        if lock1 == lock2 :
            if User.objects.filter(username=name).exists():
                messages.warning(request,'username is already exists')
                return redirect('userapp:register')
            else:
                user=User.objects.create_user(first_name=f_name,last_name=l_name,username=name,email=mail,password=lock1)
                user.save()
                return redirect('userapp:login')
        else:
            messages.warning(request,'passwords are not matching')
            return redirect('userapp:register')

        return redirect('shopapp:index')

    return render(request,'register.html')

def UserProfile(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form_user=ProfileForm(request.POST or None,instance=current_user)
        if form_user.is_valid():
            form_user.save()
            return redirect('userapp:account')
    else:
        messages.info(request,'you must be loggin')
        return redirect('userapp:profile')

    return render(request,'profile.html',{'form_user':form_user})



def Login(request):
    if request.method == 'POST':
        name=request.POST['username']
        lock=request.POST['password1']
        user=auth.authenticate(username=name,password=lock)
        if user is not None:
            auth.login(request,user)
            return redirect('shopapp:index')
        else:
            messages.error(request,'something went wrong')
            return redirect('userapp:login')

    return render(request,'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('shopapp:index')

def Account(request):
    if request.user.is_authenticated:
        prfile=Profile.objects.get(user__id=request.user.id)
    return render(request,'account.html',{'profile':prfile})