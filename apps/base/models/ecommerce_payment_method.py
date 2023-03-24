from django.db import models
from ..models.base import BaseModel


class EcommercePaymentMethod(BaseModel):

    name = models.CharField('Name', max_length=50, blank=False, null=False, unique=True)
    vtex_id = models.CharField('Vtes ID', max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'

    def __str__(self):
        return self.name
