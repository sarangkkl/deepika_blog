from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from accounts.models import Profile,Follow
from django.db.models import Q



# Create your views here.

def login_page(request):
    return render(request,'accounts/login.html')

def register_page(request):
    return render(request,'accounts/register.html')

def signup_handle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        avatar = request.FILES.get('avatar')
        if password == password2:
            if authenticate(request,username=username,password=password):
                messages.error(request,'Username already exists')
                return redirect('accounts/login')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                login(request,user)
                profile = Profile(user=user,image=avatar,username=username)
                profile.save()
                return redirect('/')
        else:
            messages.error(request,'Both password must be same')
            return redirect('accounts/login')
    else:
        return redirect('accounts/login')

def logout_handle(request):
    logout(request)
    return redirect('/')


def login_handle(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            messages.error(request,"Username or password is incorrect")
            return redirect('/accounts/login')
    else:
        messages.error(request,"You are not authorize to access the page")
        return redirect('/')

def searchUser(request):
    if request.method == "POST":
        key = request.POST.get('search')
        result = Profile.objects.filter(Q(username__icontains=key))
        
        count = result.count()
        context={
            'result':result,
            'count':count
        }
        return render(request,'home/searchResult.html',context)
    else:
        return redirect('/')

        
def followHandle(request,id):
    profile = Profile.objects.get(id=id)
    user = request.user
    x = Follow(user=user,following=profile.user)
    x.save()
    return redirect('/')