from django.urls import path
from . import views


urlpatterns = [
    path('allvendeur/', views.allVendeurs),
    path('getvendeur/<int:id>/', views.getVendeur),
    path('addvendeur/', views.addVendeur),
    path('updatevendeur/<int:id>/', views.updateVendeur),
    path('deletevendeur/<int:id>/', views.deleteVendeur),
]
