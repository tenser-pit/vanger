from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.urls import path, include, re_path

from .views import landing_render

app_name = 'landing'

urlpatterns = [
    path('', landing_render, name='landing'),
    re_path(r'^filer_public/', include('filer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
