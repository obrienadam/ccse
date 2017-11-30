from django import forms

from .models import Subscriber

class SubscribtionForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Subscriber
        fields = ('first_name', 'last_name', 'email')