from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^login/$', views.login_page, name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
]