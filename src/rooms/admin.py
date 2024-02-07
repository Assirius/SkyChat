from django.contrib import admin

from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Комнаты"""
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}

