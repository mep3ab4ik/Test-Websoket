from django.contrib import admin
from .models import Friend


@admin.register(Friend)
class FriendshipAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver', 'is_accepted']
    list_display = ['sender', 'receiver', 'is_accepted']
    search_fields = ['sender', 'receiver', 'is_accepted']

    class Meta:
        model = Friend