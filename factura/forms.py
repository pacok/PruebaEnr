from django import forms

from factura.models import Factura


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura

        fields = [
            'nombre',
            'adjunto',
            'checkbox',
            'licitacion',
            'contrato',
            'precio',
            'iva',
            'total',
        ]
        labels = {
            'nombre': 'Nombre',
            'fecha': 'Fecha',
            'adjunto': 'Adjunto',
            'checkbox': 'Marcar si tierne Licitacion',
            'licitacion': 'Licitacion',
            'contrato': 'Contrato',
            'precio': 'Precio',
            'iva': 'Iva',
            'total': 'Total',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
          #  'publicada': forms.BooleanField(required=False),
        }
