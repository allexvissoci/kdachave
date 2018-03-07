from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$',
        auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.index, name='home'),
    url(r'^filtro/$', views.registro_filter, name='filter'),
    url(r'propriedade/', include('propriedade.urls', namespace="propriedade")),
    url(r'pessoa/', include('pessoa.urls.pessoa', namespace="pessoa")),
    url(r'molho/', include('molho.urls', namespace="molho")),
    url(r'registro/', include('registro.urls', namespace="registro")),
    url(r'updateDashboard/', views.updateDashboard, name="updateDashboard"),
]
