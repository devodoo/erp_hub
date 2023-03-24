from ...models.currency import *
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


# class ConfCountryStateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConfCountryState
#         exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
#
#
# class ConfCurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConfCurrency
#         exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
#
#
# class ConfContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConfContact
#         exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


