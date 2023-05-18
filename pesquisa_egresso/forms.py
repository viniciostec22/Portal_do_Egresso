from django import forms
from .models import Pesquisa

class PesquisaForm(forms.ModelForm):
    telefone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'telefone-mask'}))

    class Meta:
        model = Pesquisa
        fields = '__all__'
        widgets = {
            'avaliacao_curso': forms.RadioSelect(),
            'avaliacao_aprendizado': forms.RadioSelect(),
            'sexo':forms.RadioSelect(),
            'estado_civil':forms.RadioSelect()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remover a opção vazia dos campos RadioSelect
        self.fields['avaliacao_curso'].choices = [('ruim', 'Ruim'), ('media', 'Média'),('bom', 'Bom'), ('otimo', 'Otimo')]
        self.fields['avaliacao_aprendizado'].choices = [('ruim', 'Ruim'), ('media', 'Média'),('bom', 'Bom'), ('otimo', 'Otimo')]
        self.fields['sexo'].choices = [('M', 'Masculino'), ('F', 'Feminino')]
        self.fields['estado_civil'].choices = [('solteiro', 'Solteiro'), ('casado', 'Casado'),('divorciado', 'Divorciado'),('viuvo', 'Viúvo'),]
   
