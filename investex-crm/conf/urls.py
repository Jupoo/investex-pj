"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from apps.clients.views import ClientsView
from apps.dashboard.views import DashboardView
from apps.events.views import EventsView

crm_patterns = [
    path('', RedirectView.as_view(url=reverse_lazy('dashboard'))),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('clients/', ClientsView.as_view(), name='clients'),
    path('events/', EventsView.as_view(), name='events'),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(crm_patterns)),
]
