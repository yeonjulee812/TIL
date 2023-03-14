from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Django PJT</h1>")

def templates(request):
    return render(request, 'firstapp/index.html')

def templates2(request):
    return render(request, 'firstapp/index2.html')

def first(request):
    name = '이연주'
    job = '학생'
    menus = ['햄버거', '제육', '치킨']
    title = 'mY nAmE iS YEONju'
    context = {
      'name': name,
      'job': job,
      'menus': menus,
      'title': title
    }
    
    return render(request, 'firstapp/first.html', context)