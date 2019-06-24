from django.conf.urls import url

from moodPosts.views import MoodPostAPIView


urlpatterns = [
    url(r'^$', MoodPostAPIView.as_view(), name='post-listcreate'),
]