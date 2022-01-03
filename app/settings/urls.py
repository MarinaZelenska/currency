
import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import (
    TemplateView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('currency/', include('currency.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('api/v1/', include('api.v1.urls')),

    path('silk/', include('silk.urls', namespace='silk')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
