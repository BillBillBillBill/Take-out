from django.conf.urls import url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
#router.register(r'seller', views.SellerViewSet)
# router.register(r'store', views.StoreViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'seller/(\d*)', views.SellerDetail.as_view()),
    url(r'seller', views.SellerList.as_view()),
    url(r'store/(\d*)', views.StoreDetail.as_view()),
    url(r'store', views.StoreList.as_view()),
    url(r'food/(\d*)', views.FoodDetail.as_view()),
    url(r'food', views.FoodList.as_view()),
    # url(r'store/$', views.StoreList.as_view()),
]
