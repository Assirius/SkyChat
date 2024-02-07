from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите E-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['email'].label = 'E-mail'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Повтор пароля'

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "w-full mt-2 px-4 py-2 rounded-xl"

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})
                               )
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
                               )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "w-full  mt-2 px-4 py-2 rounded-xl"


    class Meta:
        model = get_user_model()
        fields = ("username", "password")
