from rest_framework.routers import DefaultRouter

from . import viewSets

router = DefaultRouter()
router.register(r'investigadores', viewSets.InvestigadoresViewSet, basename="listar_investigadores")
router.register(r'reportes_adm', viewSets.ReportesAdmViewSet, basename="reportes_enviados")

urlpatterns = router.urls