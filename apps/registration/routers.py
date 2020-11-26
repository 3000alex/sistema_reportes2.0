from rest_framework.routers import DefaultRouter

from . import viewSet 

router = DefaultRouter()
router.register(r'perfil', viewSet.UserViewSet, basename="perfil")

urlpatterns = router.urls