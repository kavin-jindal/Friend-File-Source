from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from kavinblog.models import Profile


class ProfilePageForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('bio','profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url')
    
    widgets = {'bio': forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Enter you bio'}),
        'website_url': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Link to your website'}),
        'facebook_url': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Link to your facebook'}),
        'instagram_url': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Link to your instagram'}),
        'twitter_url': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Link to your twitter profile'}),




    }





class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your Email ID'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your Last Name'}))
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your Email ID'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your Last Name'}))
    '''
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your Last Name'}))
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs = {'class' : 'form-check', 'placeholder' : 'Enter your Last Name'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs = {'class' : 'form-check', 'placeholder' : 'Enter your Last Name'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs = {'class' : 'form-check', 'placeholder' : 'Enter your Last Name'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your Last Name'}))
    '''
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs = {'class' : 'form-control','type': 'password', 'placeholder' : 'Enter your old password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs = {'class' : 'form-control','type': 'password', 'placeholder' : 'Enter your new password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs = {'class' : 'form-control','type': 'password', 'placeholder' : 'Confirm your new password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')