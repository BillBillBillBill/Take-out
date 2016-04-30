import views
from django.conf.urls import url


urlpatterns = [
    url(r'customer/(\d*)', views.CustomerDetail.as_view()),
    url(r'customer', views.CustomerList.as_view()),
    url(r'delivery_information/(\d*)', views.DeliveryInformationDetail.as_view()),
    url(r'delivery_information', views.DeliveryInformationList.as_view()),
    url(r'complaint/(\d*)', views.ComplaintDetail.as_view()),
    url(r'complaint', views.ComplaintList.as_view()),
]
