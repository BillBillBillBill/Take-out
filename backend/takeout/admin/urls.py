import views
from django.conf.urls import url


urlpatterns = [
    url(r'admin/(\d*)', views.AdminDetail.as_view()),
    url(r'admin', views.AdminList.as_view()),
]
