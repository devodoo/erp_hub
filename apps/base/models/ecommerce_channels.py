from django.db import models
from ..models.base import BaseModel


class EcommerceChanel(BaseModel):

    name = models.CharField('Name', max_length=50, blank=False, null=False, unique=True)
    vtex_id = models.CharField('Vtes ID', max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name
