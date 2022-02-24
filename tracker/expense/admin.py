from django.contrib import admin

from tracker.expense.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass