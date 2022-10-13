from django.http import HttpResponse
from django.shortcuts import render
from quiz1.models import contestant

x = contestant.objects.raw('SELECT id,email,pwd FROM quiz1_contestant')
emails = []
passwords = []
for i in x:
    emails.append(i.email)
    passwords.append(i.pwd)



def index(request):
    return render(request, 'index.html')

def signup(request):
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    if email not in emails:
        savingdata = contestant(email = email, pwd = password)
        savingdata.save()
        return HttpResponse("Registered")
    else:
        return HttpResponse("Already Exist!!")

def login(request):
    return render(request, 'login.html')

def logch(request):
    email = request.POST.get('email')
    password = request.POST.get('pwd')

    if email not in emails:
        return HttpResponse("Wrong Credentials!!")
    else:
        if password not in passwords:
            return HttpResponse("Wrong Credentials!!")
        else:
            return render(request, 'portal.html')
