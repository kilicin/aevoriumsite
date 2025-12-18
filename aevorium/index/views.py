from django.shortcuts import render

def index(request):
    data = {'totalonline': 5252, 'online_rp': 100}
    return render(request, 'index/index.html', data)

def registration(request):
    return render(request, 'index/registration.html')

def login(request):
    return render(request, 'index/login.html')

def shop(request):
    return render(request, 'index/shop.html')