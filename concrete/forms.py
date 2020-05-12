from django import forms
from concrete.models import AlbumImage
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumImage
        exclude = []

    zip = forms.FileField(required=False)

class modalTicket(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    name = forms.CharField(min_length=3,
                               max_length=200,
                               required=True,
                               help_text='Длина логина должна быть не меньше 3-х и не больше 20',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form34', 'name':'name'}),
                               )
    email = forms.EmailField(max_length=255,
                                required=True,
                                widget=forms.EmailInput(attrs={'class': 'form-control validate', 'id': 'form29', 'name':'email'}),
                                help_text='Это поле обязательно')
    tel = forms.CharField(min_length=6,
                                max_length=11,
                                widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'form8', 'name':'tel', 'type': 'tel'}),
                               )
    message = forms.CharField(min_length=3,
                                max_length=2000,
                                help_text='Длина логина должна быть не меньше 3-х и не больше 20',
                                widget=forms.Textarea(attrs={'class': 'md-textarea form-control', 'id': 'form7', 'name':'message', 'rows': '3'}),
                                )

    class Meta:
        fields = ('name', 'email', 'phone', 'message', 'captcha')

    

