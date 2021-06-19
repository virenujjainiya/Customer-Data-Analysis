
from django.shortcuts import redirect, render, resolve_url
from .forms import Registrationform
from django.contrib.auth.views import LoginView,LogoutView, redirect_to_login  

class loginview(LoginView):
    template_name = 'login.html'

class logoutview(LogoutView):
    template_name = 'logout.html'


def  home_view(request):
   

    return render(request,'home.html',{})

def registerview(request):

    form=Registrationform(request.POST or None)
    error=None

    if request.method == "POST":

        form=Registrationform(request.POST)
        if form.is_valid():
           form.save()
           return redirect('login')
            
        else:
            error='invalid details'    
    else:
        form=Registrationform()

    context={
            'form':form,
            'error':error
        }
    
    return render(request,'register.html',context)




def  card1_view(request):
   

    return render(request,'card1.html',{})
    
def  card2_view(request):
   

    return render(request,'card2.html',{})

def  card3_view(request):
   

    return render(request,'card3.html',{})

def card4_view(request):
   

    return render(request,'card4.html',{})

def  card5_view(request):
   

    return render(request,'card5.html',{})


def  card6_view(request):
   

    return render(request,'card6.html',{})

