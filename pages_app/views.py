from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePagesView(TemplateView):
    template_name='pages/home.html'


class AboutPagesView(TemplateView):
    template_name='pages/about.html'