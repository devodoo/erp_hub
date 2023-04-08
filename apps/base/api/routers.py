from rest_framework.routers import DefaultRouter

from .viewset.hub_viewset import *
from .viewset.brand_viewset import *
from .viewset.category_viewset import *
from .viewset.warehouse_viewset import *
from .viewset.payment_method_viewset import *
from .viewset.country_viewset import *
from .viewset.state_viewset import *
from .viewset.channel_viewset import *
from .viewset.currency_viewset import *
from .viewset.contact_viewset import *

router = DefaultRouter()

router.register(r'hub', EcommerceHubViewSet, basename='hubs')
router.register(r'brand', EcommerceBrandViewSet, basename='brands')
router.register(r'category', EcommerceCategoryViewSet, basename='categories')
router.register(r'warehouse', EcommerceWarehouseViewSet, basename='warehouses')
router.register(r'payment_method', EcommercePaymentMethodViewSet, basename='payment_methods')
router.register(r'country', EcommerceCountryViewSet, basename='countries')
router.register(r'state', EcommerceStateViewSet, basename='states')
router.register(r'channel', EcommerceChannelViewSet, basename='channels')
router.register(r'currency', EcommerceCurrencyViewSet, basename='currencies')
router.register(r'contact', EcommerceContactSerializer, basename='contacts')

urlpatterns = router.urls