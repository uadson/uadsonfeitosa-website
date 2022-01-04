from django.urls import path

from website.views.home_view import TestView


app_name = 'website'

urlpatterns = [
	path('', TestView.as_view(), name="test"),
]