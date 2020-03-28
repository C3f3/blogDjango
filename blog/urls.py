from django.conf.urls import include,url
from . import views

urlpatterns = [
    #la cadena debe coincidir con inicio y final
    #la unica cadena que va a coincidir es vacio
    #post_list es lan funcion que renderiza la plantilla html
    url(r'^$',views.post_list),
]