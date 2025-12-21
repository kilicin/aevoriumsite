from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from mcstatus import JavaServer
from .models import Users, Servers

def index(request):
    data = {
        'servers': [],
        'totalonline': 0,
    }
    i = 0
    for server in Servers.objects.all():
        try:
            serv = JavaServer.lookup(server.ip)
            status = serv.status()
            data['servers'] += [[server.name, status.players.online, True, server.description]]
            data['totalonline'] += status.players.online
        except ConnectionRefusedError:
            data['servers'] += [[server.name, '---', False]]
            data['totalonline'] += 0

    return render(request, 'index/index.html', data)

def registration(request):
    try:
        user = Users.objects.get(token=request.session['token'])
        if 'token' in request.session:
            if user.token == request.session['token']:
                return redirect('personal-cabinet')
    except (ValueError, Users.DoesNotExist, KeyError):
        if request.method == 'POST':
            if request.POST['password'] == request.POST['password-verify']:
                Users.objects.create(email=request.POST["email"],
                                     nickname=request.POST["login"],
                                     password=make_password(request.POST["password"]),
                                     token=request.POST['csrfmiddlewaretoken'])
    return render(request, 'index/registration.html')

def login(request):
    if request.method == "POST":
        try:
            user = Users.objects.get(nickname=request.POST['login'])
        except Users.DoesNotExist:
            data = {
                'error': True,
            }
            return render(request, 'index/login.html', data)
        if check_password(request.POST['password'], user.password):
            request.session['token'] = user.token
            return redirect('personal-cabinet')
    return render(request, 'index/login.html')

def shop(request):
    return render(request, 'index/shop.html')

def personal_cabinet(request):
    data = {}
    if request.method == 'POST':
        if 'exit' in request.POST:
            request.session.flush()
            return redirect('login')
    try:
        user = Users.objects.get(token=request.session['token'])
        data = {
            "login": user.nickname,
        }
        return render(request, 'index/personal-cabinet.html', data)
    except (ValueError, Users.DoesNotExist):
        return render(request, 'index/personal-cabinet.html', data)

def start(request):
    return render(request, 'index/start.html')

def forgotPassword(request):
    return render(request, 'index/forgot-password.html')

def newPassword(request):
    return render(request, 'index/new-password.html')

def deposit(request):
    return render(request, 'index/deposit.html')