from django.db import models
from apps.base.models import BaseModel
from apps.base.models.ecommerce_measure_unit import EcommerceMeasureUnit
from apps.base.models.ecommerce_brand import EcommerceBrand
from apps.base.models.ecommerce_warehouse import EcommerceWarehouse
from apps.base.models.ecommerce_category import EcommerceCategory


class EcommerceProductTemplate(BaseModel):

    name = models.CharField('Name', max_length=150, unique=True, blank=False, null=False)
    sku = models.CharField('SKU', max_length=150, unique=True, blank=False, null=False)
    price = models.FloatField('Price')
    description = models.TextField('Descripción de Producto', blank=False, null=False)
    image = models.ImageField('Product image', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(EcommerceMeasureUnit, on_delete=models.CASCADE, verbose_name='MeasureUnit', null=True)
    category_product = models.ForeignKey(EcommerceCategory, on_delete=models.CASCADE,
                                         verbose_name='Category', null=True)
    brand = models.ForeignKey(EcommerceBrand, on_delete=models.CASCADE,
                                         verbose_name='Brand', null=True)
    warehouse = models.ForeignKey(EcommerceWarehouse, on_delete=models.CASCADE,
                              verbose_name='Warehouse', null=True)

    height = models.FloatField('High')
    length = models.FloatField('Length')
    width = models.FloatField('width')
    reward_value = models.IntegerField('Reward value')
    manufacturer_code = models.CharField('Manufacture code', max_length=150, blank=False, null=False)
    modal_type = models.CharField('Modal type', max_length=150, blank=False, null=False)
    commercial_condition_id = models.IntegerField('Condition of the commercial Id')
    unit_multiplier = models.IntegerField('Unit multiplier')
    kit_itens_sell_apart = models.BooleanField('Can be sale alone')
    is_active = models.BooleanField('Activate')
    is_activate_if_possible = models.BooleanField('Activate if is possible')
    ref_id = models.CharField('Reference', max_length=150, blank=False, null=False)
    vtex_id = models.CharField('Vtex ID', max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = 'Product template'
        verbose_name_plural = 'Product templates'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.sku}'
