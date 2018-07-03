from django.conf.urls import url
from user.api import views


urlpatterns = [
    url(r'^$', views.users),
    url(r'^(?P<pk>\d+)/$', views.user_detail),
]
