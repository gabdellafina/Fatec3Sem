from django import forms
from appHome.models import Usuario

class FormCadastroUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
