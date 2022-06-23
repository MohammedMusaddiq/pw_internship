from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    error_message = forms.UserCreationForm.error_messages.update(
        {
            "duplicate_email": (
                "This email has already been taken."
            )
        }
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        email = self.cleaned_data["email"]

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise ValidationError(
            self.error_messages["duplicate_email"]
        )
