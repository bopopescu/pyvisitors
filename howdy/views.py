from django.http import HttpResponse
from django.shortcuts import render

def view(request):
  return render(request,'use_main.html')

def url_name(request):
	return render(request,'base.html')


def show(request):
	return render(request,'index.html')