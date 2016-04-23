from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from bussiness.serializers import SellerSerializer, StoreSerializer
from models.seller import Seller
from models.store import Store
from rest_framework.response import Response


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


# class StoreList(APIView):
#     def get(self, request, format=None):
#         stores = Store.objects.all()
#         serializer = StoreSerializer(stores, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = StoreSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
