from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import home, shop , shop_cart, checkout,contact ,about, shop_category , product

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('shop/<int:category_id>/', shop_category, name='shop'),


   
    path('product/<int:product_id>/', product, name='shop-details'),
    path('shopping-cart/', shop_cart, name='shopping-cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),

    path('about/', about, name='about'),
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)