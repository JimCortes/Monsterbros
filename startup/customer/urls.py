from rest_framework.routers import DefaultRouter
from .views import Customer

router = DefaultRouter()
router.register(r'customers', Customer, basename='customers')
urlpatterns = router.urls
