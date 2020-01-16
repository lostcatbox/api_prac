from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]