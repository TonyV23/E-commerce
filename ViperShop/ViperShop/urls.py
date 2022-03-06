from django.contrib import admin
from django.urls import path
from store.views import index ,product_detail
from accounts.views import signup
from django.conf.urls.static import static
from ViperShop import settings


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),    
    path('product/<str:slug>/', product_detail, name='product'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
