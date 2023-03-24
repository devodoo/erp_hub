from django.db import models
from apps.base.models import BaseModel, EcommerceHub
from ..models.ecommerce_product_product import EcommerceProductProduct


class EcommerceProductContent(BaseModel):

    name = models.CharField('Name', max_length=150, unique=True, blank=False, null=False)
    product = models.ForeignKey(EcommerceProductProduct, on_delete=models.CASCADE,
                                verbose_name='Product', null=True)
    platform = models.ForeignKey(EcommerceHub, on_delete=models.CASCADE,
                              verbose_name='Platform', null=True)
    name_sku = models.CharField('Name sku', max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.name_sku}'
