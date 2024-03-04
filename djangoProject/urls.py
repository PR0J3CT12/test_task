from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="djangoProject API",
        default_version='1.0.0',
        description="API documentation of djangoProject",
    ),
    public=True,
    url=''
)

urlpatterns = [
    path('api/mail/', include('mail.urls')),
    path('api/docs', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
]
