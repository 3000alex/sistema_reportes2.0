from django.urls import path
from . import views as vista #apoyo_institucional,desarrollo_tec_inovacion,formacion_RH,home,informacion_adicional,investigacion_cientifica,perfil


reportespatterns = ([
    #Biblioteca
    path('biblioteca-personal', vista.biblioteca_personal.as_view(), name="biblioteca_personal"),
    path('busqueda-ads', vista.busqueda_ads.as_view(), name="busqueda_biblioteca"),
    #Rutas de API ADS
    path('publicaciones-generales', vista.publicaciones_generales.as_view(), name="publicaciones_generales"),
    path('agregar-biblioteca',vista.agregar_biblioteca.as_view(), name="agregar-biblioteca"),

    #Secciones
    path('reporte-productividad',vista.reporte_productividad.as_view(), name='reporte-productividad'),
    path('Ampliar-sesion',vista.ampliarSesion.as_view(), name="Ampliar-sesion"),
    path('apoyo-institucional', vista.apoyo_institucional.as_view(), name="apoyo_institucional"),
    path('desarrollo-tec-inovacion', vista.desarrollo_tec_inovacion.as_view(), name="DTI"),
    path('formacion-RH', vista.formacion_RH.as_view(), name="formacion_RH"),
    path('informacion-adicional', vista.informacion_adicional.as_view(), name="informacion_adicional"),
    path('home', vista.home.as_view(), name="home"),
    path('investigacion-cientifica', vista.investigacion_cientifica.as_view(), name="investigacion_cientifica"),    
    #Operaciones de las secciones  
    
    #reporte de productividad
    path('generarReporte',vista.generarReporte.as_view(), name="generarReporte"),
    path('reportesEnviados', vista.reportesEnviados.as_view(), name="reportesEnviados"),
    #Investigacion cientifica
    path('info-anteriorModelo1',vista.infoAnteriorModelo1.as_view(), name="info-anteriorModelo1"),
    path('info-anteriorModelo2',vista.infoAnteriorModelo2.as_view(), name="info-anteriorModelo2"),
    path('info-anteriorModelo3',vista.infoAnteriorModelo3.as_view(), name="info-anteriorModelo3"),
    path('info-anteriorModelo4',vista.infoAnteriorModelo4.as_view(), name="info-anteriorModelo4"),

    #Formacion RRHH - CRUD
    path('info-anteriorModelo5',vista.infoAnteriorModelo5.as_view(), name="info-anteriorModelo5"),
    path('info-anteriorModelo6',vista.infoAnteriorModelo6.as_view(), name="info-anteriorModelo6"),
    path('info-anteriorModelo7',vista.infoAnteriorModelo7.as_view(), name="info-anteriorModelo7"),
    path('info-anteriorModelo8',vista.infoAnteriorModelo8.as_view(), name="info-anteriorModelo8"),
    path('info-anteriorModelo9',vista.infoAnteriorModelo9.as_view(), name="info-anteriorModelo9"),
    path('info-anteriorModelo10',vista.infoAnteriorModelo10.as_view(), name="info-anteriorModelo10"),
    path('info-anteriorModelo11',vista.infoAnteriorModelo11.as_view(), name="info-anteriorModelo11"),
    path('info-anteriorModelo12',vista.infoAnteriorModelo12.as_view(), name="info-anteriorModelo12"),
    path('info-anteriorModelo13',vista.infoAnteriorModelo13.as_view(), name="info-anteriorModelo13"),
    path('info-anteriorModelo14',vista.infoAnteriorModelo14.as_view(), name="info-anteriorModelo14"),
    path('info-anteriorModelo15',vista.infoAnteriorModelo15.as_view(), name="info-anteriorModelo15"),
    path('info-anteriorModelo16',vista.infoAnteriorModelo16.as_view(), name="info-anteriorModelo16"),
    path('info-anteriorModelo17',vista.infoAnteriorModelo17.as_view(), name="info-anteriorModelo17"),
    path('info-anteriorModelo18',vista.infoAnteriorModelo18.as_view(), name="info-anteriorModelo18"),

    #Finalizar reporte
    path('enviar-Reporte',vista.enviarReporte.as_view(), name="enviar-Reporte")
    
],'reportes')
