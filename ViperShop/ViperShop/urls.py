from django.contrib import admin
from django.urls import path
from store.views import index ,product_detail
from accounts.views import signup, logout_user,login_user,add_to_cart
from django.conf.urls.static import static
from ViperShop import settings


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),    
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart', add_to_cart, name='add-to-cart'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
