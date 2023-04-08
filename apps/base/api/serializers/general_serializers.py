from ...models import Currency, EcommerceMeasureUnit, EcommerceBrand, EcommerceCategory, \
    EcommerceWarehouse, EcommerceCountry, EcommercePaymentMethod, EcommerceChanel, EcommerceHub, EcommerceContact, EcommerceState
from rest_framework import serializers


class EcommerceHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceHub
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommerceBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceBrand
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


# class UpdateEcommerceBrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EcommerceBrand
#         fields = ('username', 'email', 'name', 'last_name')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommerceMeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceMeasureUnit
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommerceBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceBrand
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommerceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceCategory
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        unique_together = ('slug', 'parent',)


class EcommerceWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceWarehouse
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommerceCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceCountry
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class EcommerceCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommerceStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceState
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommercePaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommercePaymentMethod
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommerceChanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceChanel
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EcommerceContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceContact
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')




