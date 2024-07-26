from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),
    # http://127.0.0.1:8000/myapp/
    path("myapp/", include("myapp.urls", namespace="myapp")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

