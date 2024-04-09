from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

# def register(request):
#     return render(request, 'register.html')

# def user_maintenance(request):
#     return render(request, 'user_maintenance.html')

def user_page(request, user_name):
    return HttpResponse(f'<h1>{user_name}\'s</h1>')

def number_page(request, user_name, number):
    user_name = user_name.upper()
    return HttpResponse(f'<h1>{user_name}\'s page number = {number}</h1>')

def my_view(request):
    # メッセージを追加
    messages.add_message(request, messages.INFO, 'Your message here.')
    return render(request, 'my_template.html')




