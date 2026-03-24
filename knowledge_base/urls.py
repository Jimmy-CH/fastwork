from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.KnowledgeCategoryViewSet)
router.register(r'articles', views.KnowledgeArticleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

