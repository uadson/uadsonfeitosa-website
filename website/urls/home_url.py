from django.urls import path

from website.views.home_view import HomeView


app_name = 'website'

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
]