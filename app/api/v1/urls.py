from django.conf.urls import url
from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from . import views
from .views import SourceApiView

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('rates', views.RateViewSet, basename='rate')
router.register('contacts', views.ContactUsViewSet, basename='contacts')

urlpatterns = [path('source/list/', SourceApiView.as_view(), name='source_list'),
               path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
               # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
               url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
               url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
               url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
               ]

urlpatterns += router.urls
