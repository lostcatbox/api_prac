"""api_prec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 #prefix이름은 바뀌어도 상관없음
    path('api-token-auth/', obtain_auth_token),

    path('sample/', include('sample.urls'), name='sample'),
    path('ep03/', include('ep03.urls'), name='ep03'),
    path('ep04/', include('ep04.urls'), name='ep04'),
    path('ep06/', include('ep06.urls'), name='ep06'),
    path('ep08/', include('ep08.urls'), name='ep08'),
    path('api/', include('api.urls'), name='api'),
]
