from cgitb import text
from django.shortcuts import render
# httpRequest return data to client
from django.http import HttpResponse
from . import models

# Create your views here.
#  Views function perform request or return web reponse
def index(request):
    currentcies = {'usd':12345,'eur':234,'jpy':3231,'aud':3231} #database
    return render(request, 'firstapp\index.html',{'bien_a':123,'currentcies':currentcies})

def read_number(request,number=None):
    text = f"<h3>The number is {number}</h3>" 
    return HttpResponse(text)
def read_year(request,year):
    return HttpResponse('Nam ban nhap la : ' + str(year))

def page(request,number = 1):
    return HttpResponse('So page ban nhap: ' + str(number))

def read_websites(request):
    # import model
    # from . import models
    weblist = models.Website.objects.order_by('name')
    return render(request,'firstapp/websites.html',context={'website':weblist})
