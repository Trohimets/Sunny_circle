from rest_framework.serializers import ModelSerializer

from src.contacts.models import ContactsPage


class ContactsPageSerializer(ModelSerializer):
    class Meta:
        model = ContactsPage
        fields = (
            'id',
            'address',
            'phone',
            'email',
            'working_time',
            'working_day',
        )
