from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('post/', views.post_list),
    # path('post/<int:pk>', views.post_detail),
]