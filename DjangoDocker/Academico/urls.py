from django.urls import path, include
from . import views

from rest_framework import routers 
router = routers.DefaultRouter()
router.register('curso', views.CursoView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso)
]