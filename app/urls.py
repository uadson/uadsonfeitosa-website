from django.urls import path

from app.views.home import HomeView


app_name = 'app'

urlpatterns = [
    # home
    path('', HomeView.as_view(), name='home'),
]
