from django.urls import path

from website.views.home import post_list
from website.views.detail import post_detail


app_name = 'website'

urlpatterns = [
    path('', post_list, name="post_list"),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        post_detail,
        name='post_detail'),
    
]