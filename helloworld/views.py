from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.template import loader

def index(request):
	template = loader.get_template('guestbookver1.html')
	names = ['pecu', 'michael', 'domi']
	context = { 'names': names,
				'fulltext': 'how are you'}
	return HttpResponse(template.render(context, request))
	#return render(request, 'guestbookver1.html')