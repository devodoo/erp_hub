from django.db import models
from ..models.base import BaseModel
from ..models.ecommerce_country import EcommerceCountry


class EcommerceState(BaseModel):

    name = models.CharField('Name', max_length=50, blank=False, null=False, unique=True)
    code_state = models.CharField('Code country', max_length=4, blank=False, null=False, unique=True)
    country = models.ForeignKey(EcommerceCountry, on_delete=models.CASCADE, verbose_name='Country')
    vtex_id = models.CharField('Vtes ID', max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name

