from django.db import models
from apps.base.models import BaseModel
from ..models.choices import gender
from ..models.ecommerce_country import EcommerceCountry
from ..models.ecommerce_state import EcommerceState

type_contact = (
    ('provider', 'Provider'),
    ('client', 'Client'),
)


class EcommerceContact(BaseModel):

    names = models.CharField(max_length=150, verbose_name='Name')
    last_name = models.CharField(max_length=150, verbose_name='Last name')
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Address')
    street_door_number = models.CharField(max_length=150, null=True, blank=True, verbose_name='Street door number')
    floor = models.CharField(max_length=150, null=True, blank=True, verbose_name='Floor')
    apartment = models.CharField(max_length=150, null=True, blank=True, verbose_name='Apartment')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Location')
    between_street = models.CharField(max_length=150, null=True, blank=True, verbose_name='Between Street')
    zip = models.CharField(max_length=10, null=True, blank=True, verbose_name='Zip')
    sex = models.CharField(max_length=10, choices=gender, default='male', verbose_name='Sex')
    email = models.EmailField('Email address', max_length=255, unique=True)
    image = models.ImageField('Imagen', upload_to='perfil/', max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='Phone')
    country = models.ForeignKey(EcommerceCountry, on_delete=models.CASCADE, verbose_name='Country')
    state = models.ForeignKey(EcommerceState, on_delete=models.CASCADE, verbose_name='State', null=True, blank=True)
    contact_type = models.CharField(max_length=10, choices=type_contact, verbose_name='Contact type')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['names']
