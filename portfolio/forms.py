from django import forms


class User_Registration(forms.Form):

    email = forms.EmailField(help_text="Valid Email Required")
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class PortfolioForm(forms.Form):
    name = forms.CharField(max_length=100)
    header = forms.CharField(widget=forms.Textarea)
    style = forms.ChoiceField(widget=forms.Select(), choices=[('1','Light'),('2','Dark')])

