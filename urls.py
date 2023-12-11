"""
URL configuration for Distribuidora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from DistribuidoraCarne import views
from django.contrib import admin
from django.urls import path
from DistribuidoraCarne.views import FacturaDetailView, descargar_pdf_factura, FacturaListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('factura/<int:pk>/', FacturaDetailView.as_view(), name='factura_detail'),
    path('factura/', FacturaListView.as_view(),name="Lista"),
    path('descargar_pdf_factura/<int:id>/', views.descargar_pdf_factura, name='descargar_pdf_factura'),
]

