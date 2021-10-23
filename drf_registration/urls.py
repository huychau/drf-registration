from django.urls import path

from drf_registration import api

urlpatterns = [
    path('login/', api.LoginView.as_view(), name='login'),
    path('login/social/', api.SocialLoginView.as_view(), name='login_social'),
    path('logout/', api.LogoutView.as_view(), name='logout'),
    path('register/', api.RegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', api.ActivateView.as_view(), name='activate'),
    path('verify/', api.VerifyView.as_view(), name='verify'),
    path('profile/', api.ProfileView.as_view(), name='profile'),
    path('change-password/', api.ChangePasswordView.as_view(), name='change_password'),
    path('reset-password/', api.ResetPasswordView.as_view(), name='reset_password'),
    path(
        'reset-password/<uidb64>/<token>/',
        api.ResetPasswordConfirmView.as_view(),
        name='reset_password_confirm'
    ),
    path(
        'reset-password/complete/',
        api.ResetPasswordCompleteView.as_view(),
        name='reset_password_complete'
    ),
    path('set-password/', api.SetPasswordView.as_view(), name='set_password'),
]
