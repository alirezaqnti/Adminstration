
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^__debug__/', include('debug_toolbar.urls')),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path('',include('Panel.urls')),
    path('admins/',include('Admins.urls')),
]
