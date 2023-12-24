from django.db import models
from filer.fields.image import FilerImageField
from django.utils.html import mark_safe
from easy_thumbnails.files import get_thumbnailer

class Image(models.Model):
    name = models.CharField(max_length=32)
    image = FilerImageField(on_delete=models.CASCADE)
    custom_order = models.PositiveIntegerField(default=0, db_index=True)

    def image_tag(self):
        if self.image:
            options = {'size': (45, 45), 'crop': True}
            image_url = get_thumbnailer(self.image).get_thumbnail(options).url
            return mark_safe(f'<img src="{image_url}"/>')
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    class Meta:
        ordering = ['custom_order']
        verbose_name = 'изображение'
        verbose_name_plural = 'Изображения'