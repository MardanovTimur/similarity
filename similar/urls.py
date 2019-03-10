from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from similar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    url(r'^recommend/(?P<id>[0-9]+)$', views.recommendation, name="recom"),
    url(r'^friends/(?P<id>[0-9]+)$', views.user_friends, name="friends"),
    url(r'^users$', views.users, name="recom"),
    url(r'^indrecom/from/(?P<from_id>[0-9]+)/to/(?P<to_id>[0-9]+)$', views.individual_recom, name="indrecom"),
]
