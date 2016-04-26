# coding: utf-8
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from bussiness.serializers import SellerSerializer, StoreSerializer
from models.seller import Seller
from models.store import Store
from rest_framework.response import Response
from lib.utils.response import JsonResponse, JsonErrorResponse
from lib.utils.misc import gen_update_dict_by_list
from django.db import models


class SellerList(APIView):
    def get(self, request):
        # 获取卖家列表
        sellers = [seller.to_string() for seller in Seller.objects.all()]
        return JsonResponse({"seller_list": sellers})

    def post(self, request):
        # 注册
        username = request.json.get("username")
        password = request.json.get("password")
        nickname = request.json.get("nickname")
        account_type = request.json.get("account_type")
        if not all([username, password, nickname, account_type]):
            return JsonErrorResponse("username, password, nickname, account_type are needed", 400)
        new_seller = Seller(
            username=username,
            password=password,
            nickname=nickname,
            account_type=account_type
        )
        try:
            new_seller.save()
        except Exception, e:
            print e
            return JsonErrorResponse("Fail")
        print "新注册id：", new_seller.id
        print request.data
        print request.query_params
        return JsonResponse({"id": new_seller.id})


class SellerDetail(APIView):
    def get(self, request, seller_id):
        print seller_id
        print request.json
        try:
            seller = Seller.objects.get(id=seller_id)
        except Seller.DoesNotExist:
            return JsonErrorResponse("Seller does not exist", 404)
        return JsonResponse({"seller": seller.to_detail_string()})

    def put(self, request, seller_id):
        update_item = ['nickname', 'password']
        update_dict = gen_update_dict_by_list(update_item, request.json)
        modify_num = Seller.objects.filter(id=seller_id).update(**update_dict)
        if modify_num == 1:
            return JsonResponse({})
        print request.json
        print request.query_params
        return JsonErrorResponse("Update failed", 400)


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def perform_create(self, serializer):
        if self.request.account_type != 'bussiness':
            print 'Wrong Account Type'
            return
        serializer.save(owner=self.request.u)


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
