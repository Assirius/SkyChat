from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:room_detail", kwargs={"room_slug": self.slug})

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ('create_at', )

