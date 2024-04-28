# Formulario de opiniones

from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['titulo', 'contenido', 'autor', 'puntaje']  # Asegúrate de que los campos que quieres que se muestren en el formulario estén aquí
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'puntaje': forms.Select(attrs={'class': 'form-control'}),
        }