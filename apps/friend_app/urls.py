from django.conf.urls import url
from . import views
app_name = 'friend'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^log_out$', views.log_out, name='log_out'),
    url(r'^add_friend$', views.add_friend_page, name='add_friend_page'),
    url(r'^add/(?P<friend_id>\d+)$', views.add_friend, name='add_friend'),
    url(r'^friends$', views.friend_list, name='friend_list'),
    url(r'^unfriend/(?P<friend_id>\d+)$', views.unfriend, name='unfriend'),
]
