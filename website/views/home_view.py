from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView


class HomeView(TemplateView):
	
	template_name = 'website/home.html'