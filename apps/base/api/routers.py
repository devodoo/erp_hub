from rest_framework.routers import DefaultRouter

from .viewset.hub_viewset import *
from .viewset.brand_viewset import *
from .viewset.category_viewset import *

router = DefaultRouter()

router.register(r'hub', EcommerceHubViewSet, basename='hubs')
router.register(r'brand', EcommerceBrandViewSet, basename='brands')
router.register(r'category', EcommerceCategoryViewSet, basename='categories')

urlpatterns = router.urls