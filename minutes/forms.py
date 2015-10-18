from django import forms

from .models import User

class RegisterForm(forms.Form):
    class Meta:
        model = User
        fields = ['userName', 'password', 'email']

    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    Password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    def clean(self):
        pass1 = self.cleaned_data.get('Password1')
        pass2 = self.cleaned_data.get('Password2')

        if pass1 and pass1 != pass2:
            raise forms.ValidationError("Passwords do not match.")

        return self.cleaned_data





class SignUpForm(forms.Form):
    class Meta:
        model = User
        fields = ['userName', 'email', 'password']

    def clean_userName(self):
        userName = self.cleaned_data.get('userName')
        # write validation code
        return userName

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        # domain, extension = provider.split(".")
        # # if not domain == "USC":
        # #     raise forms.ValidationError("Please make sure you use your USC email.")
        # if not extension == "edu":
        #     raise forms.ValidationError("Please use a valid .edu email address")
        return email

