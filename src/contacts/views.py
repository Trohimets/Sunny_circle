from rest_framework import viewsets

from src.contacts.models import ContactsPage
from src.contacts.serializers import ContactsPageSerializer


class ContactsPageViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Контакты
    '''
    queryset = ContactsPage.objects.all()
    serializer_class = ContactsPageSerializer
