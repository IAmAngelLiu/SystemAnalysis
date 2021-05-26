from django import forms
# from django.contrib.auth.models import User
from .models import Member

class LoginForm(forms.Form):
    username = forms.CharField(label='使用者帳號')
    password = forms.CharField(widget=forms.PasswordInput, label='密碼')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密碼', widget=forms.PasswordInput)
    password2 = forms.CharField(label='請再輸入一次密碼', widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('username', 'name', 'email', 'address', 'cellphone', 'password', 'password2')
        labels = {
            'username': '使用者帳號', 
            'name': '姓名', 
            'email': 'Email', 
            'address': '地址', 
            'cellphone': '手機號碼'
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('兩次輸入的密碼不同。')
        return cd['password2']
