from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('apps.account.urls')),
    path('api/category/', include('apps.category.urls')),
    path('api/products/', include('apps.product.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
