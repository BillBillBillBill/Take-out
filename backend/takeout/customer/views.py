# coding: utf-8
from rest_framework.views import APIView
from models.customer import Customer, DeliveryInformation
from models.complaint import Complaint
from bussiness.models.store import Store
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


# 收货信息
class DeliveryInformationList(APIView):
    def get(self, request):
        # 获取收货信息列表
        customer = request.u
        if not customer:
            return JsonErrorResponse("can't find customer", 404)
        delivery_informations = [delivery_information.to_string() for delivery_information in customer.delivery_informations.all()]
        return JsonResponse({"delivery_information_list": delivery_informations})

    def post(self, request):
        # 添加收货信息
        owner = request.u
        address = request.json.get("address")
        phone = request.json.get("phone")
        receiver = request.json.get("receiver")
        if not all([address, phone, receiver]):
            return JsonErrorResponse("address, phone, receiver are needed", 400)
        new_delivery_information = DeliveryInformation(
            address=address,
            phone=phone,
            receiver=receiver,
            customer=owner,
        )
        try:
            new_delivery_information.save()
        except Exception, e:
            print e
            return JsonErrorResponse("Fail" + e.message)
        print "新收货信息id：", new_delivery_information.id
        return JsonResponse({"id": new_delivery_information.id})


class DeliveryInformationDetail(APIView):
    def get(self, request, delivery_information_id):
        try:
            delivery_information = DeliveryInformation.objects.get(id=delivery_information_id)
        except DeliveryInformation.DoesNotExist:
            return JsonErrorResponse("DeliveryInformation does not exist", 404)
        return JsonResponse({"delivery_information": delivery_information.to_detail_string()})

    def put(self, request, delivery_information_id):
        # 更新收货信息
        try:
            owner = request.u
            update_item = ['address', 'phone', 'receiver']
            update_dict = get_update_dict_by_list(update_item, request.json)
            modify_num = owner.delivery_informations.filter(id=delivery_information_id).update(**update_dict)
            assert modify_num == 1
            return JsonResponse({})
        except Exception, e:
            return JsonErrorResponse("Update failed:" + e.message, 400)

    def delete(self, request, delivery_information_id):
        # 删除食品
        try:
            result = DeliveryInformation.objects.get(id=delivery_information_id).delete()
            assert result[0] == 1
            return JsonResponse({})
        except Exception, e:
            return JsonErrorResponse("Delete failed:" + e.message, 400)


# 投诉
class ComplaintList(APIView):
    def get(self, request):
        # 获取投诉列表
        customer = request.u
        if not customer:
            return JsonErrorResponse("can't find customer", 404)
        complaints = [complaint.to_string() for complaint in customer.complaints.all()]
        return JsonResponse({"complaint_list": complaints})

    def post(self, request):
        # 添加投诉
        try:
            owner = request.u
            content = request.json.get("content")
            store_id = request.json.get("store_id")
            store = Store.objects.get(id=store_id)
            if not all([content, store]):
                return JsonErrorResponse("content, store_id are needed", 400)
            new_complaint = Complaint(
                content=content,
                store=store,
                customer=owner,
            )
            new_complaint.save()
        except Exception, e:
            print e
            return JsonErrorResponse("Fail" + e.message)
        print "新投诉id：", new_complaint.id
        return JsonResponse({"id": new_complaint.id})


class ComplaintDetail(APIView):
    def get(self, request, complaint_id):
        try:
            complaint = Complaint.objects.get(id=complaint_id)
        except Complaint.DoesNotExist:
            return JsonErrorResponse("Complaint does not exist", 404)
        return JsonResponse({"complaint": complaint.to_detail_string()})

    def put(self, request, complaint_id):
        # 更新投诉
        try:
            update_item = ['status']
            update_dict = get_update_dict_by_list(update_item, request.json)
            modify_num = Complaint.objects.filter(id=complaint_id).update(**update_dict)
            assert modify_num == 1
            return JsonResponse({})
        except Exception, e:
            return JsonErrorResponse("Update failed:" + e.message, 400)
