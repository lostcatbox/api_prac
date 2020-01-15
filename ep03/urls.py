from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
]