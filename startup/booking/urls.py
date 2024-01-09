from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, TruckViewSet, AppointmentViewSet, AppointmentsApiView

router = DefaultRouter()

router.register(r'branches', BranchViewSet, basename='branch')
router.register(r'trucks', TruckViewSet, basename='truck')
router.register(r'appointments', AppointmentViewSet, basename='appointment')


urlpatterns = [
   # path('', include(router.urls)),
    path('api/appointments_view/<int:year>/<int:month>/<int:day>/<int:pk>/', AppointmentsApiView.as_view(), name='appointments'),

    # Add the detail route URL pattern
    path('api/branches/<int:pk>/details/', BranchViewSet.as_view({'get': 'details_by_pk'}), name='branch-details-by-pk'),
    path('api/trucks/<int:pk>/', TruckViewSet.as_view({'get': 'retrieve'}), name='truck-detail'),
    path('api/appointments/<int:pk>/', AppointmentViewSet.as_view({'get': 'retrieve'}), name='appointment-detail'),
]

urlpatterns += router.urls