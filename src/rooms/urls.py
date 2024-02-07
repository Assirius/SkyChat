from django.urls import path

from . import views

app_name = "rooms"

urlpatterns = [
    path("", views.RoomListView.as_view(), name="rooms_list"),
    path("<slug:room_slug>/", views.RoomDetailView.as_view(), name="room_detail"),
]
