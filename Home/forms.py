from django import forms
from ckeditor.widgets import CKEditorWidget

from Home.models import *

class Forms_cms(forms.Form):
    seu_campo_rich_input = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Apresentacao
        fields = '__all__'
    