from django import forms

class DadosEmailForm(forms.Form):
    nome = forms.CharField(max_length=250)
    fone = forms.CharField(max_length=11)
    email = forms.CharField(max_length=150)
    mensagem = forms.CharField(widget=forms.Textarea)

