"""
ASGI config for stockproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os 

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application 
from channels.auth import AuthMiddlewareStack
from mainapp.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')

application = ProtocolTypeRouter({
  
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
    URLRouter(
      websocket_urlpatterns
    )
  )
  # Just HTTP for now. (We can add other protocols later.)
})
