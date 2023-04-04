from django.db import models
from ..models.base import BaseModel
from ..models.choices import platform


class EcommerceHub(BaseModel):

    name = models.CharField('Name', max_length=50, blank=False, null=False, unique=True)
    platfrom = models.CharField('Platform', choices=platform, max_length=50, blank=False, null=False, default='vtex')
    api_key = models.CharField('Api Key', max_length=500, blank=True, null=True)
    api_token = models.CharField('Api token', max_length=1000, blank=True, null=True)
    url = models.CharField('Url', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Hub'
        verbose_name_plural = 'Hubs'

    def __str__(self):
        return self.name
