#!/usr/bin/python env
# -*- coding:utf-8 -*-
# author : Chen Zhipeng
#date:2018/6/11 8:52

from django import forms
from django.forms import fields

class PlotFrom(forms.Form):
    price = forms.CharField()
