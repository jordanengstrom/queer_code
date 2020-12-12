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
from core.views import IndexTemplateView
from .routers import router
from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

# Email verification setup documentation:
# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [
    # admin site
    path('admin/', admin.site.urls),

    # user related paths
    # Custom version of RegistrationView provided by Django
    path('accounts/register/', RegistrationView.as_view(form_class=CustomUserForm, success_url='/'),
         name='django-registration-register'),
    # Other urls Django needs
    path('accounts/', include('django_registration.backends.one_step.urls')),
    # Used to login users via the browser
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('users.api.urls')),
    # Login for browseable api
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^.*$', IndexTemplateView.as_view(), name='entry-point'),

    # app related paths
    path('', include(router.urls)),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]
