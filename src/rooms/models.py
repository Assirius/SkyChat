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
