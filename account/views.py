from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetConfirmView
from .forms import CustomSetPasswordForm

User = get_user_model()

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'email/password_reset_confirm.html'  # Replace with your template path
    form_class = CustomSetPasswordForm  # Use the custom form here

    def post(self, request, *args, **kwargs):
        # Call Django's built-in post method to handle password reset confirmation
        response = super().post(request, *args, **kwargs)

        # Check if the password reset was successful
        if response.status_code == 302:
            # Redirect the user to the desired webpage after password reset
            return redirect('password_reset_complete')  # Replace with your desired webpage URL

        return response