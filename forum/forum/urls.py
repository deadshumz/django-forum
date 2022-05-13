from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('auth/', include('users.urls')),
    path('', include('users.urls')),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
