from django.db.models import Q
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.friends import FriendsSerializer, WaitFriendsSerializer
from ...models import Friend


class FriendsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    """
    GET: Показывает список друзей авторизованного пользователя
    POST: Отправка запроса в друзья. Указываем только 'id' получаемого пользователя
    """
    serializer_class = FriendsSerializer
    queryset = Friend.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            (Q(sender=self.request.user) | Q(receiver=self.request.user))
        )


class WaitFriendsViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin):
    """
    GET:
    PATH: Принимаем запрос в друзья.
    Для принятия в друзья переводим поле 'wait_answer' в False(0), а поле is_accepted в True(1)
    Для отклонения запроса используем метод DELETE
    """
    serializer_class = WaitFriendsSerializer
    queryset = Friend.objects.filter(wait_answer=True)

    def get_queryset(self):
        return self.queryset.filter(receiver=self.request.user)


class RemoveFriendsViewSet(GenericViewSet, DestroyModelMixin):
    """
    DELETE:
        1. Когда пользователь отклоняем заявку в друзья
        2. Удаление из списка друзей
    """
    serializer_class = FriendsSerializer
    queryset = Friend.objects.all()
