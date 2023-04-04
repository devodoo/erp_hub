from django.db import models
from ..models.base import BaseModel
from ..models.ecommerce_hub import EcommerceHub
from ..models.choices import state


class EcommerceBrand(BaseModel):

    name = models.CharField('Name', max_length=50, blank=True, null=True)
    vtex_id = models.CharField('Vtex ID', max_length=250, blank=True, null=True)
    title = models.CharField('Title', max_length=250, blank=True, null=True)
    link = models.CharField('Link ID', max_length=250, blank=True, null=True)
    active = models.BooleanField('Active', max_length=250, blank=False, null=False, default=True)
    description = models.TextField('Active', max_length=250, blank=True, null=True)
    state = models.CharField(max_length=10, choices=state, default='pending',
                                      verbose_name='State')
    platform = models.ForeignKey(EcommerceHub, on_delete=models.CASCADE, verbose_name='Platform', null=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name
