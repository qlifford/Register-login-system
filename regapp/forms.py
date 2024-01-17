from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegForm(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields = ('username','email',)

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper
        #     self.helper.form_method = 'post'
        #     self.helper.add_input(Submit())