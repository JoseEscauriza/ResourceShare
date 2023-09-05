from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def home_page(request):
    response = "<html><h1>Welcome to ResourceShare</h1></html>"
    return HttpResponse(response)


class HomePage(TemplateView):
    template_name = 'home_page.html'
