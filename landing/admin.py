from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'image', 'custom_order', 'image_tag']