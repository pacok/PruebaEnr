from django import forms

from contrato.models import Contrato


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato

        fields = [
            'nombre',
            'fecha',
            'licitacion'
        ]
        labels = {
            'nombre': 'Nombre',
            'fecha': 'Fecha',
            'licitacion': 'Licitacion'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
          #  'fecha' : forms.DateTimeInput,
            'licitacion' : forms.Select(attrs={'class':'form-control'}),
        }