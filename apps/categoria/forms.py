from django import forms
from .models import Categoria

def agregarFormControl(campos):
    for camposVisibles in campos:
        camposVisibles.field.widget.attrs['class'] = 'form-control'

class FormularioCategria(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormularioCategria, self).__init__(*args, **kwargs)
        # Agregar campos
        agregarFormControl(self.visible_fields())
        
    nombre_categoria = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'otraclase otraclase otraclase otraclase'
            }
        )
    )
    class Meta:
        model = Categoria
        fields =  '__all__'
