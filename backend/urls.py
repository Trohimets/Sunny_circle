from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from src.assistance.views import JobViewSet
from src.contacts.views import ContactsPageViewSet
from src.center.views import VolunteersViewSet, CenterPageViewSet, \
    SpecialistsPageViewSet, SpecialistsViewSet, \
    VolunteersPageViewSet, SchoolViewSet, WorkshopsViewSet, \
    KindergartenViewSet, EisViewSet, EducationalSiteViewSet
from src.main_page.views import MainPageViewSet
from src.assistance.views import ReportTypeViewSet

admin.site.site_header = 'Администрирование сайта "Солнечный круг"'
admin.site.site_title = "Администрирование сайта"
admin.site.index_title = "Добро пожаловать!"

router = DefaultRouter()
router.register('center/school', SchoolViewSet)
router.register('center/workshops', WorkshopsViewSet)
router.register('center/kindergarten', KindergartenViewSet)
router.register('center/eis', EisViewSet)
router.register('contacts', ContactsPageViewSet)
router.register('assistance/jobs', JobViewSet)
router.register('assistance/reports', ReportTypeViewSet)
router.register('center/specialists-page', SpecialistsPageViewSet)
router.register('center/specialists', SpecialistsViewSet)
router.register('center/volunteers', VolunteersViewSet)
router.register('center/volunteers-page', VolunteersPageViewSet)
router.register('center/educational-site', EducationalSiteViewSet)
router.register('center', CenterPageViewSet)
router.register('', MainPageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cookies/', include('src.approval_cookies.urls')),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
