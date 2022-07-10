from django.urls import path, include

from .views import index, friend
from friends_app.api.views.router import api_routers


urlpatterns = [
    # path('', index, name="index"),
    # path('friend', friend, name="friend"),
    path('api/', include(api_routers.urls)),
]