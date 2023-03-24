from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers.general_serializers import *
from ...models.currency import Currency
# from rest_framework.decorators import action

# from apps.sale.security.permisions import IsOwner

# from rest_framework.pagination import PageNumberPagination
#
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 4

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class CountryViewSet(viewsets.ModelViewSet):
    model = Currency
    serializer_class = CountrySerializer
    queryset = Currency.objects.all()
    permission_classes = (IsAuthenticated,)


# class ConfCountryStateViewSet(viewsets.ModelViewSet):
#     model = ConfCountryState
#     serializer_class = ConfCountryStateSerializer
#     queryset = ConfCountryState.objects.all()
#     permission_classes = (permissions.IsAuthenticated, IsOwner,)
#
#
# class ConfCurrencyViewSet(viewsets.ModelViewSet):
#     serializer_class = ConfCurrencySerializer
#     queryset = ConfCurrency.objects.all()
#     permission_classes = (permissions.IsAuthenticated, IsOwner,)
#
#
# class ConfContactViewSet(viewsets.ModelViewSet):
#     serializer_class = ConfContactSerializer
#     queryset = ConfContact.objects.all()
#     permission_classes = (permissions.IsAuthenticated, IsOwner,)


