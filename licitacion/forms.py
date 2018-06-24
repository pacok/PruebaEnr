from django import forms

from licitacion.models import Licitacion


class LicitacionForm(forms.ModelForm):
    class Meta:
        model = Licitacion

        fields = [
            'nombre',
            'publicada',
        ]
        labels = {
            'nombre': 'Nombre',
            'publicada': 'Publicada',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
          #  'publicada': forms.BooleanField(required=False),
        }
