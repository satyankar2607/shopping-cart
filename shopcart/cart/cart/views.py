from django.http import HttpResponse
from django.shortcuts import render
from cart1.models import peop
from cart1.models import cartitem
from cart1.models import custdata

x = custdata.objects.raw('SELECT id,email,pwd FROM cart1_custdata')
emails = []
passwords = []
for i in x:
    emails.append(i.email)
    passwords.append(i.pwd)

def index(request):
    return render(request, 'index.html')
def index1(request):
    return render(request, 'index1.html')
def login(request):
    return render(request, 'login.html')

def signup(request):
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    if email not in emails:
        savingdata = custdata(email = email, pwd = password)
        savingdata.save()
        return HttpResponse("Registered")
    else:
        return HttpResponse("Already Exist!!")
def logch(request):
    email = request.POST.get('email')
    password = request.POST.get('pwd')

    if email not in emails:
        return HttpResponse("Wrong Credentials!!")
    else:
        if password not in passwords:
            return HttpResponse("Wrong Credentials!!")
        else:
            return render(request, 'index.html')

def adm(request):
    return render(request,'adm.html')
def user(request):
    q = peop.objects.all()
    content = {"message": q}
    return render(request,'user.html',content)
def add(request):
    product = request.POST.get('product')
    price = request.POST.get('price')
    Savingdata = peop(product = product , price = price)
    Savingdata.save()
    return HttpResponse("Item added!")
def upd(request):
    product = request.POST.get('product')
    price = request.POST.get('price')
    peop.objects.filter(product = product).update(price = price)
    return HttpResponse("price updated")
def dele(request):
    product = request.POST.get('product')
    peop.objects.filter(product = product).delete()
    return HttpResponse("product deleted")
def showlist(request):
    r=peop.objects.all()
    content={"message":r}
    return render(request,"showlist.html",content)
def showcart(request,product,price):
    hey = cartitem(product = product,price = price)
    hey.save()
    return HttpResponse("ITEM ADDED")
def mycart(request):
    r = cartitem.objects.all()
    content={"message":r}
    return render(request,"mycart.html",content)
def delcart(request,product):
    cartitem.objects.filter(product = product).delete()
    return HttpResponse("ITEM DELETED")
def tot(request):
    sum = 0
    for i in cartitem:
        sum = sum + int(i.price)
    content = {"message":sum}
