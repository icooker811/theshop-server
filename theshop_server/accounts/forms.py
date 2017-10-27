from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(label=u'username',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label=u'password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
