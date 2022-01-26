from django.urls import path

from website.views.home import post_list


app_name = 'website'

urlpatterns = [
    path('', post_list, name="post_list"),
    
]
