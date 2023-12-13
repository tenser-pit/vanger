from django.db import models
from filer.fields.image import FilerImageField
from django.utils.html import mark_safe


class Image(models.Model):
    name = models.CharField(max_length=32)
    image = FilerImageField(null=False, blank=False, on_delete=models.CASCADE)
    custom_order = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    class Meta:
        ordering = ['custom_order']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'