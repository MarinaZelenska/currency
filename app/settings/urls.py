
import debug_toolbar

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('currency/', include('currency.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),

    path('silk/', include('silk.urls', namespace='silk')),



]
