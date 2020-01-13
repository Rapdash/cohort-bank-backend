from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('branches.urls')),
    path('auth/', include('knox.urls'))
]
