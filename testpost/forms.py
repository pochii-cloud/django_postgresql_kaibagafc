from django import forms

from testpost.models import Joined


class JoinForm(forms.ModelForm):
    class Meta:
        model = Joined
        fields = '__all__'
