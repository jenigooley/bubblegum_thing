from django.conf.urls import url, include
from allauth.account.views import LoginView
from allauth.account import views as allauthviews

from . import views

app = "comics"
urlpatterns = [
    # ex: /comic/,
    url(r'^$', allauthviews.login),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='comic-detail'),
    url(r'^(add+)/$', views.ComicAdd.as_view(), name='comic-add'),
    url(r'^(?P<pk>[0-9]+)/$', views.ComicUpdate.as_view(), name='comic-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ComicDelete.as_view(), name='comic-delete'), 
]

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<comic_id>[0-9]+)/$', views.detail, name='detail'),
# ]
