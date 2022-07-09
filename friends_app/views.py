from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def friend(request):
    return render(request, 'friend.html')