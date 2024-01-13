from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, TruckViewSet, AppointmentViewSet, NotesViewSet

router = DefaultRouter()

router.register(r'branches', BranchViewSet, basename='branch')
router.register(r'trucks', TruckViewSet, basename='truck')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'notes', NotesViewSet, basename='custom')


urlpatterns = [
   # path('', include(router.urls)),

    # Add the detail route URL pattern
    path('api/branches/<int:pk>/details/', BranchViewSet.as_view({'get': 'details_by_pk'}), name='branch-details-by-pk'),
    path('api/trucks/<int:pk>/', TruckViewSet.as_view({'get': 'retrieve'}), name='truck-detail'),
    path('api/appointments/<int:pk>/', AppointmentViewSet.as_view({'get': 'retrieve'}), name='appointment-detail'),
]

urlpatterns += router.urls