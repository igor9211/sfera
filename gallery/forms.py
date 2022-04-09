from django import forms
from .models import Gallery, Events


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image',)
