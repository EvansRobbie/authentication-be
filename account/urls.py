from django.urls import path
from .views import CustomPasswordResetConfirmView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='email/password_reset_complete.html'), name='password_reset_complete'),
]