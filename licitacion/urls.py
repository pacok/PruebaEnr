from django.conf.urls import url
from licitacion.views import licitacion, licitacion_view, licitacion_list, LicitacionList, LicitacionCreate, LicitacionUpdate, LicitacionDelete

urlpatterns = [
    url(r'^index$', licitacion, name='index'),
    url(r'^nueva$', LicitacionCreate.as_view(), name='licitacion_crear'),
    url(r'^listar$', LicitacionList.as_view(), name='licitacion_listar'),
    url(r'^editar/(?P<pk>\d+)/$', LicitacionUpdate.as_view(), name='licitacion_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', LicitacionDelete.as_view(), name='licitacion_eliminar'),
]
