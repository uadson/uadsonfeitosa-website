from django.urls import path

from website.views.detail import post_detail


app_name = 'website'

urlpatterns = [
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        post_detail,
        name='post_detail'),
]