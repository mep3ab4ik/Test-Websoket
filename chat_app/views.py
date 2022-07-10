from django.shortcuts import render


def index(request):
    return render(request, 'chat_app/index.html', {})


def room(request, room_name, token):
    return render(request, 'chat_app/room.html', {
        'room_name': room_name,
        'token': token,
    })


def login(request):
    return render(request, 'chat_app/login.html', {})
