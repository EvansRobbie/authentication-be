from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.password_validation import MinimumLengthValidator

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''

        # Add Bootstrap classes to the form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'