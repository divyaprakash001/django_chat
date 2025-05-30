from django.urls import path
from . import views

urlpatterns = [
    path("",views.createRoom,name="create-room"),
    path("room/<str:room_name>/<str:username>/",views.messageView,name="room"),
    # path("messageView",views.messageView,name="room"),
]
