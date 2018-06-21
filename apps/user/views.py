from django.shortcuts import render,redirect
import re
from apps.user import models
from django.core.urlresolvers import reverse
# Create your views here.

def Register(request):

    return render(request,'register.html')


def register_handle(reuqest):
    #进行数据提取
    username = reuqest.POST.get('user_name')
    password = reuqest.POST.get('pwd')
    email = reuqest.POST.get('email')
    allow = reuqest.POST.get('allow')
    #进行数据校验
    if not all([username,password,email]):
        return render(reuqest, 'register.html' ,{'errmsg':"数据不完整"})

    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
        return render(reuqest, 'register.html', {'errmsg': "邮箱格式不正确"})

    if allow != 'on':
        return render(reuqest, 'register.html', {'errmsg': "请同意协议"})
    try:
        user =models.User.objects.get(username=username)
    except models.User.DoesNotExist as e:
        user = None

    if user:
        return render(reuqest, 'register.html', {'errmsg': '用户名已存在'})
    #进行业务处理
    user = models.User.objects.create_user(username,email,password)
    user.is_active = 0
    user.save()
    return redirect(reverse('goods:index'))