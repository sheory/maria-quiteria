from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from web.datasets.admin import public_admin



schema_view = get_schema_view(
   openapi.Info(
      title="Maria Quiteria API",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web.home.urls")),
    path("painel/", public_admin.urls),
    path("api/", include("web.api.routes")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    re_path(r'^swagger/$', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
