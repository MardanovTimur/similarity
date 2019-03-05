from django.contrib import admin
from django.urls import path

from similar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('user/list/', views.UserList.as_view(), name='user-list'),
]
