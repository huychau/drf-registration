from django.utils.translation import gettext as _

# Email constants
DEFAULT_EMAIL_BODY = {
    'WELCOME': _('''
        <p>Hi,</p>
        <p>Welcome to the system!</p>
    '''),

    'ACTIVATE': _('''
    <p>By clicking on the following link, you are activating your account</p>
    <a href="{activate_link}">Activate Account</a>
    '''),

    'RESET_PASSWORD': _('''
    <p>Please go to the following page and choose a new password:</p>
    <a href="{reset_password_link}">Reset Password</a>
    ''')
}

# Social login
FACEBOOK_PROVIDER = 'facebook'
FACEBOOK_AUTH_URL = 'https://graph.facebook.com/v2.4/me'
FACEBOOK_FIELDS = 'email,first_name,last_name,gender,birthday'

GOOGLE_PROVIDER = 'google'
GOOGLE_AUTH_URL = 'https://oauth2.googleapis.com/tokeninfo'
