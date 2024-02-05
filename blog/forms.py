from django import forms
from .models import Denunc

class DenuncForm(forms.ModelForm):

    class Meta:
        model = Denunc
        fields = ('title', 'offender', 'offenses', 'published_date', 'image',)

