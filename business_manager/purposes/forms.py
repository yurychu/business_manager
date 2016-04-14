from django import forms

from .models import Purpose


class PurposeForm(forms.ModelForm):

    class Meta:
        model = Purpose
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PurposeForm, self).__init__(*args, **kwargs)
