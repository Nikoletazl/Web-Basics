from django import forms

from online_library.library.helpers import DisableFieldsFormMixin
from online_library.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm, DisableFieldsFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': ''
                }
            )
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class DeleteBookForm(forms.ModelForm, DisableFieldsFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = '__all__'