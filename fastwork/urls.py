"""
URL configuration for fastwork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

_app_v1_patterns = [
    path('accounts/', include('apps.accounts.urls')),
    path('customer/', include('apps.customer.urls')),
    path('service/', include('apps.service_order.urls')),
    path('product/', include('apps.product.urls')),
    path('warehouse/', include('apps.warehouse.urls')),
    path('mall/', include('apps.mall.urls')),
    path('ai/', include('apps.ai_chatbot.urls')),
    path('message/', include('apps.message_center.urls')),
    path('kb/', include('apps.knowledge_base.urls')),
    path('system/', include('apps.system_management.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(_app_v1_patterns)),

]
