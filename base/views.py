from django.shortcuts import render
#from django.http import HttpResponse
from base.models import contact

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        print(name,email,desc)
        Contact = contact(name=name, email=email, desc=desc)
        Contact.save()

    return render(request, 'base/index.html')
