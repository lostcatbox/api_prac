
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include, path

router = DefaultRouter()
router.register(r'posts', views.PostViewSet) # 이렇게 posts는 url프리픽스로 지정하면 posts/하면 목록나오고 posts/{pk}하면 특정 글에대해 열림

urlpatterns = [
    path('', include(router.urls)),

]