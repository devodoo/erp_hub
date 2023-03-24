from django.db import models


class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Satete',default=True)
    created_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('write date', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Deleted date', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Model Base'
        verbose_name_plural = 'Models Base'