from django.urls import path, include
from . import views

urlpatterns = [
    path('post/', views.post_list),
]