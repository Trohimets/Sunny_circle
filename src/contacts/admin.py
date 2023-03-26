from django.contrib import admin

from src.contacts.models import ContactsPage


@admin.register(ContactsPage)
class ContactsPageAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'phone',
        'email',
        'working_time',
        'working_day',
    )
