"""queer_code URL Configuration

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
from django.urls import path, re_path, include
# my view still renders it so I don't think this warning error is accurate
from core.views import IndexTemplateView
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
    # path('api/', include(router.urls)),
]
