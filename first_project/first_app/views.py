from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def user_maintenance(request):
    return render(request, 'user_maintenance.html')

def user_page(request, user_name):
    return HttpResponse(f'<h1>{user_name}\'s</h1>')

def number_page(request, user_name, number):
    user_name = user_name.upper()
    return HttpResponse(f'<h1>{user_name}\'s page number = {number}</h1>')




