from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, error_messages={'invalid':"Entrez un mail valide"})
     

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        













        """ def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields["email"].error_messages.update = {'invalid': 'Custom Error Message'} """

        """ error_messages = {
            'password2': {
                'password_entirely_numeric': "Votre mdp ne peut etre uniquement chiffre",
            },
        } """

""" 
        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)

        # add custom error messages
            self.fields['name'].error_messages.update({
                'invalid': 'Entrez un mail valide',
            }) """





   
""" first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        labels = {
            "username":"Pseudo :",
            "email":"Email :",
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user """