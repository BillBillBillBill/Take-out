"""takeout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from lib.controllers.session_controller import login
from lib.controllers.file_manager import file_uploader
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api-token-auth/(.*)', login),
    url(r'upload', file_uploader),
    url(r'', include('bussiness.urls')),
    url(r'', include('customer.urls')),
    url(r'', include('admin.urls')),
]
urlpatterns += staticfiles_urlpatterns()
