from django import forms
from .models import Pesquisa

class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = '__all__'
