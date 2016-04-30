import views
from django.conf.urls import url


urlpatterns = [
    url(r'customer/(\d*)', views.CustomerDetail.as_view()),
    url(r'customer', views.CustomerList.as_view()),
]
