from django.shortcuts import HttpResponse

from django.shortcuts import render

from .models import Greeting

def index(request):
    return HttpResponse("Hello World!")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})