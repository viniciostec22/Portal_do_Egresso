from django import forms
from .models import Pesquisa
AVALIACAO_CURSO_CHOICES = [
    ('ruim', 'Ruim'),
    ('media', 'Média'),
    ('bom', 'Bom'),
    ('otimo', 'Ótimo'),
]
AVALIACAO_APRENDIZADO_CHOICES = [
    ('ruim', 'Ruim'),
    ('media', 'Média'),
    ('bom', 'Bom'),
    ('otimo', 'Ótimo'),
]
SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

ESTADO_CIVIL_CHOICES = [
    ('solteiro', 'Solteiro'),
    ('casado', 'Casado'),
    ('divorciado', 'Divorciado'),
    ('viuvo', 'Viúvo'),
]
class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = '__all__'
        widgets = {
            'avaliacao_curso': forms.RadioSelect(),
            'avaliacao_aprendizado': forms.RadioSelect(),
        }
# class PesquisaForm(forms.ModelForm):
    
    # avaliacao_curso = forms.MultipleChoiceField(
    #     choices=AVALIACAO_CURSO_CHOICES,
    #     widget=forms.RadioSelect,
    #     required=False  # O campo não é obrigatório
    # )
    # avaliacao_aprendizado = forms.MultipleChoiceField(
    #     choices=AVALIACAO_APRENDIZADO_CHOICES,
    #     widget=forms.RadioSelect,
    #     required=False
    # )
    
    # sexo = forms.MultipleChoiceField(
    #     choices=SEXO_CHOICES,
    #     widget=forms.RadioSelect,
    #     required=False
    # )
    
    # estado_civil = forms.MultipleChoiceField(
    #     choices=ESTADO_CIVIL_CHOICES,
    #     widget=forms.RadioSelect,
    #     required=False
    # )

    # class Meta:
    #     model = Pesquisa
    #     fields = '__all__'
