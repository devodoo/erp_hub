from rest_framework.routers import DefaultRouter

from .viewset.general_viewset import *

router = DefaultRouter()

router.register(r'countries', CountryViewSet, basename='countries')

urlpatterns = router.urls