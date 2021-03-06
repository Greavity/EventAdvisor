from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm

from django.forms import Form
from accounts.models import User


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass


class SubmittablePasswordChangeForm(SubmittableForm, PasswordChangeForm):
    pass


class SignUpForm(SubmittableForm, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['login_email', 'name', 'city']

