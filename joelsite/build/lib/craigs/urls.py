from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^(?P<job_name_id>[0-9]+)$', views.settings, name='settings'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),

    #url(r'^(?P<job_name_id>[0-9]+)/active/$', views.active, name='active'),
    url(r'^new-task$', views.create_task, name='create_task'),
]