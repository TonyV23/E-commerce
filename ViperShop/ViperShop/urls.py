from django.contrib import admin
from django.urls import path
from store.views import index
from django.conf.urls.static import static

from ViperShop import settings


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
