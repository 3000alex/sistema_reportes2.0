from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register(r'numerales', viewsets.Numerales, basename="Numerales")
router.register(r'modelo1', viewsets.modelo1, basename="modelo1")
router.register(r'modelo2', viewsets.modelo2, basename="modelo2")
router.register(r'modelo3', viewsets.modelo3, basename="modelo3")
router.register(r'modelo4', viewsets.modelo4, basename="modelo4")
router.register(r'modelo5', viewsets.modelo5, basename="modelo5")
router.register(r'modelo6', viewsets.modelo6, basename="modelo6")
router.register(r'modelo7', viewsets.modelo7, basename="modelo7")
router.register(r'modelo8', viewsets.modelo8, basename="modelo8")
router.register(r'modelo9', viewsets.modelo9, basename="modelo9")
router.register(r'modelo10', viewsets.modelo10, basename="modelo10")
router.register(r'modelo11', viewsets.modelo11, basename="modelo11")
router.register(r'modelo12', viewsets.modelo12, basename="modelo12")
router.register(r'modelo13', viewsets.modelo13, basename="modelo13")
router.register(r'modelo14', viewsets.modelo14, basename="modelo14")
router.register(r'modelo15', viewsets.modelo15, basename="modelo15")
router.register(r'modelo16', viewsets.modelo16, basename="modelo16")
router.register(r'modelo17', viewsets.modelo17, basename="modelo17")
router.register(r'modelo18', viewsets.modelo18, basename="modelo18")
router.register(r'citas', viewsets.citas, basename="citas")
router.register(r'reportes_finalizados', viewsets.reportes_finalizados, basename="reportes")

urlpatterns = router.urls