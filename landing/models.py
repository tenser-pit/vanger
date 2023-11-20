from django.db import models
from filer.fields.image import FilerImageField


class Image(models.Model):
    name = models.CharField(max_length=32)
    image = FilerImageField(null=False, blank=False, on_delete=models.CASCADE)
    custom_order = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True)

    class Meta:
        ordering = ['custom_order']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'