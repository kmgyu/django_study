"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# / 붙일 시, ~/pybo로 이동해도 자동으로 ~/pybo/로 이동.
# 특별한 경우가 없으면 /를 붙여주는 것이 이롭다.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/", include("pybo.urls")),
]
