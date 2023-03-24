from django.db import models
from ..models.base import BaseModel


class EcommerceBrand(BaseModel):

    name = models.CharField('Name', max_length=50, blank=False, null=False, unique=True)
    symbol = models.CharField('Symbol', max_length=3, blank=False, null=False, unique=True)
    currency = models.CharField('Currency', max_length=3, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name
