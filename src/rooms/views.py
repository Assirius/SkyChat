from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Room


class RoomListView(LoginRequiredMixin, ListView):
    """Список комнат"""
    model = Room
    template_name = "rooms/rooms-list.html"
    context_object_name = "rooms"
    extra_context = {"title": "Комнаты"}


class RoomDetailView(LoginRequiredMixin, DetailView):
    """Детальная информация о комнате"""
    template_name = "rooms/room-detail.html"
    context_object_name = "room"
    slug_url_kwarg = "room_slug"

    def get_object(self, queryset=None):
        return get_object_or_404(Room, slug=self.kwargs.get(self.slug_url_kwarg))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context.get("room").name
        return context
