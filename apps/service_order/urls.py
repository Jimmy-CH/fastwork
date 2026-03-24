from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'work-orders', views.WorkOrderViewSet)
router.register(r'feedbacks', views.FeedbackViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

