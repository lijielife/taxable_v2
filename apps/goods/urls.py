
from django.conf.urls import url
from django.contrib import admin
from apps.goods import views
from apps.goods.views import IndexView
urlpatterns = [

    url(r'^$',views.index,name='index')
]
