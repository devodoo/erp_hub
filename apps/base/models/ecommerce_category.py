from django.db import models
from ..models.base import BaseModel
from ..models.choices import mtto
from ..models.ecommerce_hub import EcommerceHub
from ..models.choices import state


class EcommerceCategory(BaseModel):

    name = models.CharField('Name', max_length=50, blank=True, null=True, unique=True)
    platform = models.ForeignKey(EcommerceHub, on_delete=models.CASCADE, verbose_name='Platform')
    parent = models.ForeignKey(
        "self",
        related_name="subcategories",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    vtex_id = models.CharField('Vtes ID', max_length=200, blank=True, null=True)
    keywords = models.CharField('Keywords', max_length=200, blank=True, null=True)
    title = models.CharField('Title', max_length=200, blank=True, null=True)
    remarketing_code = models.CharField('Remarketing Code', max_length=200, blank=True, null=True)
    global_category = models.IntegerField('ID Categoría global', blank=True, null=True)
    description = models.TextField('Description', max_length=200, blank=True, null=True)
    showing_storefront = models.BooleanField('Showing Storefront', blank=False, null=False, default=False)
    active = models.BooleanField('Active', blank=False, null=False, default=False)
    store_front_link = models.BooleanField('Store Front Link', blank=False, null=False, default=False)
    show_brand_filter = models.BooleanField('Show brand filter', blank=False, null=False, default=False)
    has_children = models.BooleanField('Has Children', blank=False, null=False, default=False)
    is_department = models.BooleanField('Is department', blank=False, null=False, default=False)
    score = models.IntegerField('Score', null=False)
    slug = models.SlugField(blank=True, null=True)
    mtto = models.CharField('Mtto', max_length=20, choices=mtto, blank=True, null=True)
    state = models.CharField(max_length=10, choices=state, default='pending',
                             verbose_name='State')

    class Meta:
        verbose_name = 'Ecommerce category'
        verbose_name_plural = 'categories'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
