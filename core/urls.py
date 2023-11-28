
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^__debug__/', include('debug_toolbar.urls')),
]
