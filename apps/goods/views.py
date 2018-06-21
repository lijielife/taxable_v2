from django.shortcuts import render

# Create your views here.

def index(reuqest):

    return render(reuqest,'index.html')