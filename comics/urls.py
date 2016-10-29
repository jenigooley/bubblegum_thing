from django.conf.urls import url, include

from . import views

app = "comics"
urlpatterns = [
    # ex: /comic/,

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/detail/x  $', views.DetailView.as_view(), name='comic-detail'),
    url(r'^(add+)/$', views.ComicAdd.as_view(), name='comic-add'),
    url(r'^(?P<pk>[0-9]+)/$', views.ComicUpdate.as_view(), name='comic-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ComicDelete.as_view(), name='comic-delete'),

]

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<comic_id>[0-9]+)/$', views.detail, name='detail'),
# ]
