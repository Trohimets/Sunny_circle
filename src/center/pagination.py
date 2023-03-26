from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationForSpecialists(LimitOffsetPagination):
    default_limit = 9
