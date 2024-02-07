from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Главная страница"""
    template_name = "core/home.html"
    extra_context = {"title": "Главная страница"}


