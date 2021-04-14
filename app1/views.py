from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index_page(request):
    return HttpResponse("Welcome")

def welcome_page(request):
    date = datetime.datetime.now()
    name = "Ravi"
    thours = int(date.strftime('%H'))
    if thours <12:
        text = "Morning"
    elif thours<6:
        text = "Afternoon"
    else:
        text = "Night"
    dic = {'dt_now':date, 'name':name, 'text':text}
    return render(request,'html/welcome.html',dic)
