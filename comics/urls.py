from django.conf.urls import url

from . import views

app = "comics"
# urlpatterns = [
#     # ex: /comic/,
#
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
# ]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<comic_id>[0-9]+)/$', views.detail, name='detail'),
]
