from django.urls import path

from .views import index, room, login

urlpatterns = [
    path('chat/', index, name='index'),
    path('login/', login, name='login'),
    path('chat/<str:room_name>/<str:token>', room, name='room'),

]
