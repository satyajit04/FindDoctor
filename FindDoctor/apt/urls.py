from django.conf.urls import url
from . import views

app_name = 'apt'

urlpatterns = [
    url(r'^$', views.make_appointment, name='make_appointment'),
    url(r'^success/$', views.apt_success, name='apt_success'),
]
