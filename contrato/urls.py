from django.conf.urls import url
from contrato.views import ContratoList, contrato, ContratoCreate, ContratoUpdate, ContratoDelete

urlpatterns = [
    url(r'^$', contrato),
    url(r'^listar$', ContratoList.as_view(), name='contrato_listar'),
    url(r'^nuevo$', ContratoCreate.as_view(), name='contrato_crear'),
    url(r'^editar/(?P<pk>\d+)/$', ContratoUpdate.as_view(), name='contrato_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', ContratoDelete.as_view(), name='contrato_eliminar'),

]
