from rest_framework import routers

from .friends import FriendsViewSet, WaitFriendsViewSet, RemoveFriendsViewSet


api_routers = routers.DefaultRouter()
api_routers.register('friends/wait', WaitFriendsViewSet)
api_routers.register('friends/remove', RemoveFriendsViewSet)
api_routers.register('friends', FriendsViewSet)


