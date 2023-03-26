from django.urls import path

from src.approval_cookies import views

__all__ = [
    'urlpatterns',
]

urlpatterns = [
    path('', views.cookies)
]
