from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

from user.models import Admin


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
        admin = Admin.objects.filter(username=username).first()
        if check_password(userpwd,admin.password):
            request.session['admin_id'] = admin.id
            return HttpResponseRedirect(reverse('article:index'))
        else:
            info = '账号或者密码错误'
            return render(request,'login.html',{'msg':info})




def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if Admin.objects.filter(username=username).exists():
            info = '账户已存在'
            return render(request,'register.html',{'msg':info})
        elif password != password2:
            info = '密码不一致'
            return render(request,'register.html',{'msg':info})
        else:
            password = make_password(password)
            Admin.objects.create(username=username,password=password)
        return HttpResponseRedirect(reverse('user:login'))





