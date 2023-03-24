from django.db import models
from ..models.base import BaseModel
from ..models.choices import mtto
from ..models.ecommerce_hub import EcommerceHub


class EcommerceCategory(BaseModel):

    name = models.CharField('Name', max_length=50, blank=False, null=False, unique=True)
    platform = models.ForeignKey(EcommerceHub, on_delete=models.CASCADE, verbose_name='Platform')
    parent = models.ForeignKey(
        "self",
        related_name="subcategories",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    vtex_id = models.CharField('Vtes ID', max_length=200, blank=False, null=False)
    keywords = models.CharField('Keywords', max_length=200, blank=False, null=False)
    title = models.CharField('Title', max_length=200, blank=False, null=False)
    remarketing_code = models.CharField('Remarketing Code', max_length=200, blank=False, null=False)
    global_category = models.CharField('ID Categoría global', max_length=200, blank=False, null=False)
    description = models.TextField('Description', max_length=200, blank=False, null=False)
    showing_storefront = models.BooleanField('Showing Storefront', blank=False, null=False)
    active = models.BooleanField('Active', blank=False, null=False)
    store_front_link = models.BooleanField('Store Front Link', blank=False, null=False)
    show_brand_filter = models.BooleanField('Show brand filter', blank=False, null=False)
    score = models.IntegerField('Score', blank=False, null=False)
    mtto = models.CharField('Score', max_length=20, choices=mtto, blank=False, null=False)

    class Meta:
        verbose_name = 'Ecommerce category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
