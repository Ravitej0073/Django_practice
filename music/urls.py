from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    url(r'^$',views.index,name='index'),
    #/music/1/
    url(r'^(?P<album_id>[\d]+)/$',views.details,name='details'),

    #music/favourite/
    url(r'^(?P<album_id>[\d]+)/favourite/$',views.favourite,name='favourite'),

]
