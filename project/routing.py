from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter
import app_chat.routing

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    # NB: The URLRouter can only contain one list of url patterns so when dealing with multiple socket apps,
    # all the url patterns must be coded in the URLRouter
    
    'websocket': AuthMiddlewareStack(
        URLRouter(
            app_chat.routing.websocket_urlpatterns
        )
    ),
})