from django import forms
from appHome.models import Produto

class FormCadastroProd(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'desc']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }