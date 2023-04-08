from django.db import models
from ..models.base import BaseModel
from ..models.choices import state


class EcommerceWarehouse(BaseModel):

    name = models.CharField('Name', max_length=50, blank=True, null=True, unique=True)
    code = models.CharField('Code', max_length=50, blank=True, null=True, unique=True)
    vtex_id = models.CharField('Vtes ID', max_length=200, blank=True, null=True)
    state = models.CharField(max_length=10, choices=state, default='pending',
                             verbose_name='State')

    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'

    def __str__(self):
        return self.name
