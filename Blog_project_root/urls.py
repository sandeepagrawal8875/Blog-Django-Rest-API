from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Blogs API",
        default_version='v1.0',
        description="A sample API for Blogs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sandeepagrawal8875@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/', include('posts.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

