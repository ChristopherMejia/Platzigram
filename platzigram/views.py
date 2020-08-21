#PLATZIGRAM VIEWS

from django.http import HttpResponse
from django.http import JsonResponse

from datetime import datetime

def hello(request):
    #return hello world
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello the time is {now}'. format(now=str(now)))

def sorted(request):
    """Ordena numeros de una lista"""
    numbers =sorted( [6,5,3,9,23] )
    #import pdb; pdb.set_trace()
    return JsonResponse(numbers, safe=False)

def hi(request, name, age):
    #return a name and age
    if age < 12:
        message ='sorry {}, you are not allowed here'.format(name)
    else:
        message = 'hello, {}! Welcome to platzigram'.format(name)

    return HttpResponse(message)