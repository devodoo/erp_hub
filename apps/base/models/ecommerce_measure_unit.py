from django.db import models
from ..models.base import BaseModel


class EcommerceMeasureUnit(BaseModel):

    name = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'

    def __str__(self):
        return self.name
