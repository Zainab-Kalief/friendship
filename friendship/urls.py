from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.user_app.urls', namespace='user')),
    url(r'^friend/', include('apps.friend_app.urls', namespace='friend')),
]
