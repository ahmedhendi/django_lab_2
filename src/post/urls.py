from django.conf.urls import url
from post import views

app_name = 'post'

urlpatterns = [
     
     url(r'^$', views.all_posts ,name="all_posts"),
     url(r'^(?P<id>\d+)$', views.get_post ,name='post'),
     url(r'^create$', views.create_post ,name='create_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post ,name='edit_post'),
    url(r'^admin$', views.admin ,name='admin'),    
     url(r'^(?P<id>\d+)/delete$', views.delete_post ,name='delete_post'),


]