from django.urls import path

from website.views.home_view import HomeView
from website.views.home_view import post_list, post_detail


app_name = 'website'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('list', post_list, name='post_list'),
    
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        post_detail,
        name='post_detail'),
]
