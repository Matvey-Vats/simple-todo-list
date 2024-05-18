from django.contrib import admin
from django.urls import path, include

from tasks.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("tasks.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

handler404 = page_not_found