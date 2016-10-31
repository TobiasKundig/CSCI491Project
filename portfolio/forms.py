from django import forms


class User_Registration(forms.Form):

    email = forms.EmailField(help_text="Valid Email Required")
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


