from django import forms
from eventos.models import InscricaoEvento

class InscricaoEventoForm (forms.ModelForm):
    class Meta:
        model = InscricaoEvento
        fields = {
            'nome',
            'email',
        }