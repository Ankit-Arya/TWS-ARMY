from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class NewUserForm(UserCreationForm):
    email  = forms.EmailField(required=True,widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email','class':'focus:outline-none'}))
    username  = forms.CharField(required=True , widget= forms.TextInput
                           (attrs={'placeholder':'Enter unique Username','class':'focus:outline-none'}))
    password1 = forms.CharField(required=True,widget= forms.PasswordInput
                           (attrs={'placeholder': 'Enter password', 'class': 'focus:outline-none', 'style': 'outline: none;'}))
    password2 = forms.CharField(required=True, widget= forms.PasswordInput
                           (attrs={'placeholder':'Re-Enter password','class':'focus:outline-none'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

    def save(self, commit = True) :
        user = super(NewUserForm,self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
