from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class Login(auth_views.LoginView):
    template_name = 'users/login.html'
    # redirect_authenticated_user = True


class Logout(auth_views.LogoutView):
    template_name = 'users/logout.html'


class PasswordChange(auth_views.PasswordChangeView):
    success_url = reverse_lazy('users:password_change_success')
    template_name = 'users/password-change.html'


class PasswordChangeSuccess(auth_views.PasswordChangeDoneView):
    template_name = 'users/password-change-success.html'


class PasswordReset(auth_views.PasswordResetView):
    email_template_name = 'users/password-reset-email.html'
    success_url = reverse_lazy('users:password_reset_sent')
    template_name = 'users/password-reset.html'


class PasswordResetSent(auth_views.PasswordResetDoneView):
    template_name = 'users/password-reset-sent.html'


class PasswordResetChange(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_success')
    template_name = 'users/password-reset-change.html'


class PasswordResetSuccess(auth_views.PasswordResetCompleteView):
    template_name = 'users/password-reset-success.html'
