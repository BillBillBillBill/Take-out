from django.conf.urls import url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'seller', views.SellerViewSet)
router.register(r'store', views.StoreViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'store/$', views.StoreList.as_view()),
]
