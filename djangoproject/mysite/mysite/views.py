from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'name' : 'satyankar', 'place' : 'jupyter'}
    return render(request, 'index.html',params)

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("DASH KI DASH ")