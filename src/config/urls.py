from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/', include('apps.cars.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
