from django.conf.urls import url
from factura.views import factura, FacturaCreate, FacturaUpdate, FacturaList, FacturaDelete

urlpatterns = [
    url(r'^$', factura),
    url(r'^nueva$', FacturaCreate.as_view(), name='factura_crear'),
    url(r'^listar$', FacturaList.as_view(), name='factura_listar'),
    url(r'^editar/(?P<pk>\d+)/$', FacturaUpdate.as_view(), name='factura_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', FacturaDelete.as_view(), name='factura_eliminar'),
]
