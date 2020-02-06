from django import forms
from concrete.models import AlbumImage

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumImage
        exclude = []

    zip = forms.FileField(required=False)