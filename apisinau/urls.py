from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='sinau api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sinau/', include("sinau.urls")),
    path('api/doc/', schema_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                    document_root=settings.MEDIA_ROOT)