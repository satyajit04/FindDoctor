from django.conf.urls import url
from . import views

app_name = 'hms'

urlpatterns = [
    url(r'^$', views.hospital_index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^hospitals/$', views.hospital_index, name='hospital_index'),
    url(r'^hospitals/(?P<pk>[0-9]+)/$', views.hospital_details, name='hospital_details'),
    url(r'^hospitals/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$', views.hospital_doctorlist, name='hospital_doctors'),
    url(r'^doctors/$', views.doctor_index, name='doctor_index'),
    url(r'^doctors/(?P<id>[0-9]+)/$', views.doctor_details, name='doctor_details'),
]
