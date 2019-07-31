from django.contrib.auth.models import User
from .models import Profile
from django import forms

# Forms

class SignUpForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_conf = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email =  forms.CharField(
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        query = User.objects.filter(username=username).exists()
        if query:
            raise forms.ValidationError('Username is already taken')
        return username
    
    def clean(self):
        """ Verify password confirmation match """
        data = super().clean()

        password = data['password']
        password_conf = data['password_conf']

        if password != password_conf:
            raise forms.ValidationError('Password confirmation does not match')
        
        return data
    
    def save(self):
        data = self.cleaned_data
        data.pop('password_conf')

        user = User.objects.create_user(**data)
        profile = Profile(user=user).save()
        

class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
    