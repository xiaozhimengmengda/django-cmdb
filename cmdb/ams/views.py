from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Ment
from .forms import NameForm, MentForm, UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.forms.models import model_to_dict
import json

@login_required
def index(request):

    return render(request,"index.html")

@login_required
def list(request):

    objects_all = Ment.objects.all()
    ret = {"objects_all": objects_all}
    return render(request,"ams/list.html",ret)

@login_required
def add(request):
    if request.method == 'POST':
        form = MentForm(request.POST)
        if form.is_valid():
            hostname = form.cleaned_data.get("hostname")
            sn = form.cleaned_data.get("sn")
            ip = form.cleaned_data.get("ip")
            mac = form.cleaned_data.get("mac")
            addr = form.cleaned_data.get("addr")
            ment = Ment(hostname=hostname, sn=sn, addr=addr, mac=mac, ip=ip)
            ment.save()
            return JsonResponse({'status': 200, 'errors': {}, 'result': {}})
        else:
            return JsonResponse({'status': 400, 'errors': json.loads(form.errors.as_json()), 'result': {}})
    else:
        form = MentForm()
    return render(request, 'ams/add.html', {'form': form})

@login_required
def delete(request, pk):
    if request.method == "GET":
        Ment.objects.filter(pk=int(pk)).delete()
        print(pk)
    return HttpResponseRedirect('/ams/list/')

@login_required
def update(request, pk):
    if request.method == "GET":
        if pk:
            rt = Ment.objects.get(pk=int(pk))
            form = MentForm(initial=model_to_dict(rt))
            return render(request, 'ams/update.html', {'form':form,"pk":pk})

    elif request.method == "POST":
        form = MentForm(request.POST)
        if form.is_valid():
            hostname = form.cleaned_data.get("hostname")
            sn = form.cleaned_data.get("sn")
            user = form.cleaned_data.get("user")
            ip = form.cleaned_data.get("ip")
            mac = form.cleaned_data.get("mac")
            ment = Ment.objects.filter(pk=int(pk))
            ment.update(hostname=hostname, sn=sn, user=user,ip=ip, mac=mac)
            return  HttpResponseRedirect('/ams/list/')
        else:
            rt = Ment.objects.get(pk=int(pk))
            form = MentForm(initial=model_to_dict(rt))
            return render(request, 'ams/update.html', {'form':form,"pk":pk})


def userlogin(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            login(request, form.cached_user)
            return HttpResponseRedirect("/ams/list/")
        else:
            return render(request, "login.html", {'form': form})
    else:
        form = UserForm()
        return render(request, "login.html", {'form': form})

@login_required
def userlogout(request):
    logout(request)
    form = UserForm()
    return render(request, 'login.html', {'form': form})





