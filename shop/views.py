from django.shortcuts import render,HttpResponse
from .models import Items,Product
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    it=Items.objects.all()
    return render(request,template_name='home.html',context={'item':it})

def u_register(request):
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pass']
        cp=request.POST['cpass']
        e=request.POST['email']
        f=request.POST['fname']
        l=request.POST['lname']

        if p==cp:
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return u_login(request)
        else:
            return HttpResponse('Passwords are not matching')
    return render(request,template_name='register.html')

def u_login(request):
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pass']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            HttpResponse('Invalid credentials')
    return render(request,template_name='login.html')

@login_required
def u_logout(request):
    logout(request)
    return u_login(request)

@login_required
def products(request,p):
    fei=Items.objects.get(category=p)
    pr=Product.objects.filter(category=fei)
    return render(request,template_name='product.html',context={'p':pr,'fei':fei})

@login_required
def details(request,p):
    ite=Product.objects.get(name=p)
    return  render(request,template_name='details.html',context={'p':ite})