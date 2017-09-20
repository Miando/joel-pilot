from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    # url(r'^(?P<job_name_id>[0-9]+)$', views.settings, name='settings'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^edit_option/$', views.edit_option, name='edit_option'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^new-task$', views.create_task, name='create_task'),
    url(r'^new-task$', views.create_task, name='create_task'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.task_delete, name='task_delete'),
]