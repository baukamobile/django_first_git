from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import *



def showPage(request):
    data = MoneySafeData.objects.all()
    return render(request, 'Mymoney/index.html',{'data':data, 'title':'Main Page'})
def about(request):
    return render(request, 'Mymoney/about.html', {'title':'about'})
def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")


def Terms(request):
    return HttpResponse('<h1>Terms and Privacy</h1>')

def OurProducts(request):
    return  HttpResponse('<h1>Our products</h1>')


def showpost(request,post_id):
    return HttpResponse(f'<h1>This is page f{post_id}</h1>')