
from django.conf.urls import url
from apps.user.views import RegisterView,LoginView,UserInfoView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^register$',RegisterView.as_view(),name='register'),#注册
    #url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    url(r'^login$',LoginView.as_view(),name='login'),#注册
    url(r'^$',login_required(UserInfoView.as_view()),name='user')
]
