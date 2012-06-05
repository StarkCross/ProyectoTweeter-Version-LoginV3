from django import forms
from main.models import Profile, Tweet

class UserForm(forms.ModelForm):
        password = forms.CharField(widget = forms.PasswordInput)
        image_owner = forms.ImageField(required=False)
 	class Meta: 
		model = Profile

class TweetForm(forms.ModelForm):
	class Meta: 
		model = Tweet

class TweetEditForm(forms.ModelForm):
        class Meta:
	    model = Tweet
            exclude = 'owner'

class UserEditForm(forms.ModelForm):
        password = forms.CharField(widget = forms.PasswordInput)
        class Meta:
            model = Profile
            exclude = ('user', 'follow')
