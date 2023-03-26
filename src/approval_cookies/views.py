from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from src.approval_cookies.models import ApprovalCookies

__all__ = [
    'cookies',
]


@extend_schema(parameters=[OpenApiParameter(name='Approval', type=str, location=OpenApiParameter.HEADER, required=True,
                                            description='Сгенерированный uid абстрактного пользователя'),
                           OpenApiParameter(name='User-Agent', type=str, location=OpenApiParameter.HEADER,
                                            required=True)])
@api_view(['POST'])
def cookies(request):
    """
    Класс для обработки соглашения пользователя об использовании cookies
    """
    response = {}
    approval_uid = None
    user_agent = None
    try:
        approval_uid = request.headers['Approval']
    except KeyError:
        response['Approval'] = 'must be'

    try:
        user_agent = request.headers['User-Agent']
    except KeyError:
        response['User-Agent'] = 'must be'

    if approval_uid and user_agent:
        try:
            ApprovalCookies.objects.create(approval_uid=approval_uid,
                                           user_agent=user_agent).save()
        except IntegrityError:
            response['detail'] = 'already exists'
            response = Response(response,
                                status=status.HTTP_409_CONFLICT)
        else:
            response['detail'] = 'ok'
            response = Response(response,
                                status=status.HTTP_201_CREATED)
    else:
        response = Response(response,
                            status=status.HTTP_400_BAD_REQUEST)

    return response
