from django.db import models
from apps.base.models import BaseModel
from ..models.currency import Currency


class EcommerceCountry(BaseModel):

    name = models.CharField('Name', max_length=50, blank=False, null=False, unique=True)
    code_country = models.CharField('Code country', max_length=4, blank=False, null=False, unique=True)
    phone_code = models.IntegerField('Code phone', blank=False, null=False, unique=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='Currency')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def __str__(self):
        return self.name
