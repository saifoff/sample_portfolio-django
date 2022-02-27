import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from new.models import Contact

from .models import Contact
# Create your views here.


def home(request):
    return render(request, 'new/home.html')
def about(request):
    return render(request, 'new/about.html')
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse('<h1>Thanks for Contract with us</h1>')
    return render(request, 'new/contact.html')
    def showdata(request):
        
        return render (request, 'showdata.html',{'Contact':data})
