from django import forms

from my_music_app.web.helpers import FormControl, DisableFields
from my_music_app.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm, FormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                },
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        albums = Album.objects.all()
        if albums:
            albums.delete()
            self.instance.delete()
        else:
            self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm, FormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class EditAlbumForm(forms.ModelForm, FormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()

    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'price': forms.NumberInput(
                attrs={
                    'step': '0.01'
                }
            )
        }


class DeleteAlbumForm(forms.ModelForm, FormControl, DisableFields):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
