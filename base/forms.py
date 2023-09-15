from django import forms
from base.models import Contato

class InscreverForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'nome',
            'email',
            'preferencia_evento',
            'observacao',
        ]