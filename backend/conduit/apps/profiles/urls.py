from django.conf.urls import url

from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

app_name = "profiles"
urlpatterns = [
    url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
    url(r'^profiles/(?P<username>\w+)/follow/?$', 
        ProfileFollowAPIView.as_view()),
]
