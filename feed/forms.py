from django import forms
from .models import Name

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=30)

    # association
    class Meta:
        fields = ('usern')
        model = Name
