from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True),
        name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/login/$', obtain_jwt_token, name='api-login'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True),
        name='login'),
    url(r'^logout/$',  auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='login'),
    url(r'^mood/', include(('moodPosts.urls', 'moodPosts'), namespace='moodPosts')),
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'),
            permanent=False), name="favicon"),
]
