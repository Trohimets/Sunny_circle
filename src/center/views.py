from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import VolunteersPage, School, Workshops, Eis, Kindergarten, EducationalSite
from .pagination import LimitOffsetPaginationForSpecialists
from .serializers import VolunteersPageSerializer, CenterSectionPageSerializer, Volunteer, CenterPage, Specialist, \
    SpecialistsPage, CenterPageSerializer, SpecialistsDetailSerializer, \
    SpecialistsListSerializer, SpecialistsPageSerializer, EducationalSiteSerializer, VolunteersListSerializer, \
    VolunteersCreateSerializer


class VolunteersViewSet(ModelViewSet):
    '''
    Класс для просмотра волонтеров
    '''
    queryset = Volunteer.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return VolunteersListSerializer
        elif self.action == 'create':
            return VolunteersCreateSerializer


class CenterPageViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Центр
    '''
    queryset = CenterPage.objects.all()
    serializer_class = CenterPageSerializer


class VolunteersPageViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Волонтеры
    '''
    queryset = VolunteersPage.objects.all()
    serializer_class = VolunteersPageSerializer


class SchoolViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Школа
    '''
    queryset = School.objects.all()
    serializer_class = CenterSectionPageSerializer


class WorkshopsViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Мастерские
    '''
    queryset = Workshops.objects.all()
    serializer_class = CenterSectionPageSerializer


class KindergartenViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Сад
    '''
    queryset = Kindergarten.objects.all()
    serializer_class = CenterSectionPageSerializer


class EisViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Служба Раннего Вмешательства
    '''
    queryset = Eis.objects.all()
    serializer_class = CenterSectionPageSerializer


class SpecialistsPageViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Специалисты
    '''
    queryset = SpecialistsPage.objects.all()
    serializer_class = SpecialistsPageSerializer


class SpecialistsViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра специалистов
    '''
    queryset = Specialist.objects.all()
    lookup_field = 'slug'
    pagination_class = LimitOffsetPaginationForSpecialists

    def get_serializer_class(self):
        if self.action == 'list':
            return SpecialistsListSerializer
        return SpecialistsDetailSerializer


class EducationalSiteViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра ссылки на образовательный сайт
    '''
    queryset = EducationalSite.objects.all()
    serializer_class = EducationalSiteSerializer
