from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AssetForm, UserForm
from .models import Asset
from datetime import datetime
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def userlogin(request):
    if request.method == "GET":
       form = UserForm()
       return render(request, "user/login.html", {'form':form})
    
    elif request.method == "POST":
         form = UserForm(request.POST)
         if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
               login(request, user)
               return HttpResponseRedirect(request.GET.get('next', '/asset/list'))

            else:
               return render(request, 'user/login.html', {'form':form})

def userlogout(request):
    logout(reqeust)
    return render(request, 'user/logout.html')

def helloworld(request):
    return HttpResponse("hello world")

@login_required
def list(request):
    rt = Asset.objects.all()
    return render(request, 'asset/list.html', {'rt':rt})

@login_required
def create(request):
    form = AssetForm(request.POST)
    rt = {'form':form}
    return render(request, 'asset/create.html', rt)
    

@login_required
def save(request):
    form = AssetForm(request.POST)
    print("form", form)
    if form.is_valid():
       username = form.cleaned_data['username']
       mac = form.cleaned_data['mac']
       os_system = form.cleaned_data['os_system']
       create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       modify_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       Asset(username=username, mac=mac, os_system=os_system, create_time=create_time, modify_time=modify_time).save()
       return  HttpResponseRedirect('/asset/list/')
    else:
       rt = {'form':form}
       return render(request, 'asset/create.html', rt)
    
@login_required
def modify(request):
    if request.method == "GET":
       id = request.GET.get('id', '')
       if id is not None:
           rt = Asset.objects.filter(pk=int(id))
           form = AssetForm()
           return render(request, 'asset/modify.html', {'rt':rt, 'form':form})

    elif request.method == "POST":
       form = AssetForm(request.POST)
       if form.is_valid():
           username = form.cleaned_data['username']
           mac = form.cleaned_data['mac']
           os_system = form.cleaned_data['os_system']
           modify_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           rt = Asset.objects.filter(mac=mac).update(username=username, os_system=os_system, modify_time=modify_time)
           
           return  HttpResponseRedirect('/asset/list/')
       else:
           rt = {'form':form}
           return render(request, 'asset/create.html', rt)

@login_required
def delete(request):
    if request.method == "GET":
       id = request.GET.get('id', '')
       if id is not None:
           Asset.objects.filter(id=int(id)).delete()
           return  HttpResponseRedirect('/asset/list/')
