from django import forms
from . models import Container

class RunContainer(forms.ModelForm):

    class Meta:
        model = Container
        fields = ('image', 'cmd')