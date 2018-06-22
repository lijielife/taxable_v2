from django.shortcuts import render,redirect
import re
from apps.user import models
from django.core.urlresolvers import reverse
# Create your views here.
from django.views.generic import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired
from taxable_v2 import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        # 进行数据校验
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': "数据不完整"})

        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': "邮箱格式不正确"})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': "请同意协议"})
        try:
            user = models.User.objects.get(username=username)
        except models.User.DoesNotExist as e:
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

            # 进行业务处理
        user = models.User.objects.create_user(username, email, password)
        user.save()

        # 发送激活邮件   格式：http：127.0.0.1/user/user_id
        # 激活链接中要包含用户的身份信息，进行加密并生成token
        # serializer = Serializer(settings.SECRET_KEY, 3600)
        # info = {'confirm':user.id}
        # token = serializer.dumps(info) #bytes
        # token = token.decode()
        #
        # subject = '后台账户测试'
        # message = ''
        # sender = settings.EMAIL_FROM
        # receiver = [email]
        # html_message = '<h1>%s 欢迎您注册</h1></br>请点击下面的链接进行用户激活</br><a href="http:127.0.0.1/user/active/%s">http:127.0.0.1/user/active/%s</a>' % (
        #     username, token, token)
        # send_mail(subject, message, sender, receiver, html_message=html_message)
        # send_mail()
        return redirect(reverse('goods:index'))

# class ActiveView(View):
#     """用户激活函数"""
#     def get(self,request,token):
#         #进行解密
#         serializer = Serializer(settings.SECRET_KEY,3600)
#         try:
#             info = serializer.loads(token)
#             user_id = info['confirm']
#             user = models.User.objects.get(id = user_id)
#             user.is_active =1
#             user.save()
#             return redirect(reverse('user:login'))
#         except SignatureExpired as e:
#             return  HttpResponse("抱歉，链接已经失效")

class LoginView(View):
    def get(self,request):
        #判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username= ''
            checked = ''
        #使用模板
        return  render(request,'login.html',{'username':username,'checked':checked})

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        if not all([username,password]):
            return render(request,'login.html',{"errmsg":"数据不完整 "})

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #判断是否需要记住用户名
                next_url = request.GET.get('next', reverse('goods:index'))
                #定义挑战下一次页面地址
                response = redirect(next_url)
                remember = request.POST.get('remember')
                if remember == 'on':
                    response.set_cookie('username',username,max_age=7*24*3600)
                else:
                    response.delete_cookie('username')
                return response

            else:
                return render(request, 'login.html',{'errmsg':"用户未激活"})
        else:
            return render(request, 'login.html',{'errmsg':"用户名或密码错误"})


class UserInfoView(View):
    def get(self, request):
        #在做用户登陆验证得时候，使用django内置得request.is_authenticated方法
        return render(request,'user_center_info.html')
    def post(self,request):
        pass


