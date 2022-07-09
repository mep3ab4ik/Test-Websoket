from rest_framework import serializers

from ...models import Friend


class WaitFriendsSerializer(serializers.ModelSerializer):
    """Сериализатор для принятия в друзья"""

    class Meta:
        model = Friend
        exclude = ['is_accepted']
        read_only_fields = ['sender', 'receiver']


class FriendsSerializer(serializers.ModelSerializer):
    """Сериализатор списка друзей и добавление в друзья """

    class Meta:
        model = Friend
        fields = ['sender', 'receiver', 'publisher_sender']
        read_only_fields = ['sender']

    publisher_sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='sender',
    )