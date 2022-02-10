from django.urls import path

from website.views.home import HomeView
from website.views.detail import post_detail


app_name = 'website'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        post_detail,
        name='post_detail'),
    
]