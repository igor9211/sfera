from django import forms
from django.contrib.auth.models import User
from .models import Child, Post


class LoginForm(forms.Form):
    name = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label="Imię")
    topic = forms.CharField(max_length=30, label="Temat")
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, label="Treść")


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email",)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie sa identyczne')

        return cd['password2']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', "email")


class ChildEditForm(forms.ModelForm):

    class Meta:
        model = Child
        fields = ('date_of_birth', 'mother_full_name', 'father_full_name', 'photo', 'information')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body', 'comments')