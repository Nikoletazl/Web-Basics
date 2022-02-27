from django import forms

from my_music_app.web.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


class FormControl:
    fields = {}

    def _init_form_control(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class DisableFields:
    disabled_fields = '__all__'
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            else:
                field.widget.attrs['readonly'] = 'readonly'
