from django.forms import ModelForm
from .models import Posts

class NameForm(ModelForm):
    # association
    class Meta:
        model = Posts
        fields = ['title', 'author', 'content']
