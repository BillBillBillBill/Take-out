# coding: utf-8
from rest_framework.views import APIView
from models.customer import Customer
from lib.utils.response import JsonResponse, JsonErrorResponse
from lib.utils.misc import get_update_dict_by_list


class CustomerList(APIView):
    def get(self, request):
        # 获取买家列表
        customers = [customer.to_string() for customer in Customer.objects.all()]
        return JsonResponse({"customer_list": customers})

    def post(self, request):
        # 注册
        username = request.json.get("username")
        password = request.json.get("password")
        nickname = request.json.get("nickname")
        account_type = request.json.get("account_type")
        if not all([username, password, nickname, account_type]):
            return JsonErrorResponse("username, password, nickname, account_type are needed", 400)
        new_customer = Customer(
            username=username,
            password=password,
            nickname=nickname,
            account_type=account_type
        )
        try:
            new_customer.save()
        except Exception, e:
            print e
            return JsonErrorResponse("Fail" + e.message)
        print "新注册顾客id：", new_customer.id
        return JsonResponse({"id": new_customer.id})


class CustomerDetail(APIView):
    def get(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return JsonErrorResponse("Customer does not exist", 404)
        return JsonResponse({"customer": customer.to_detail_string()})

    def put(self, request, customer_id):
        # 更新个人信息
        update_item = ['nickname', 'password']
        update_dict = get_update_dict_by_list(update_item, request.json)
        modify_num = Customer.objects.filter(id=customer_id).update(**update_dict)
        if modify_num == 1:
            return JsonResponse({})
        return JsonErrorResponse("Update failed", 400)
