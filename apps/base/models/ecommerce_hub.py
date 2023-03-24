from django.db import models
from ..models.base import BaseModel
from ..models.choices import platform


class EcommerceHub(BaseModel):

    name = models.CharField('Name', max_length=50, blank=False, null=False, unique=True)
    vtex_id = models.CharField('Vtes ID', max_length=200, blank=False, null=False)
    title = models.CharField('Title site', max_length=200, blank=False, null=False)
    link = models.CharField('Link', max_length=200, blank=False, null=False)
    active = models.BooleanField('Active', blank=False, null=False)
    description = models.TextField('Description', max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name
