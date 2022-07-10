# import os
#
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
#
#
# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
# })

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import friends_app.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            friends_app.routing.websocket_urlpatterns
        )
    ),
})