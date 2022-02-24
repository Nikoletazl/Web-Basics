import os

from django import forms

from tracker.expense.helpers import BootstrapFormMixin, DisableFieldsFormMixin
from tracker.expense.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image',
        }


class EditProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.image.path
        os.remove(image_path)
        self.instance.delete()
        os.remove(image_path)

        return self.instance


class Meta:
    model = Profile
    fields = ()


class CreateExpenseForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'image': forms.URLInput(),
        }


class EditExpenseForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Expense
        fields = '__all__'


class DeleteExpenseForm(forms.ModelForm, BootstrapFormMixin, DisableFieldsFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()

        return self.instance

    class Meta:
        model = Expense
        fields = '__all__'
