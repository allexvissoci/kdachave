from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'create$', views.create, name='create'),
    url(r'deletar/(?P<pk>[0-9]+)/$',
        views.DeletePropriedade.as_view(), name='delete'),
    url(r'detalhes/(?P<pk>[0-9]+)/$', views.detalhes, name='detalhe'),
    url(r'update/(?P<pk>[0-9]+)/$', views.updatePropriedade, name='update'),
]
