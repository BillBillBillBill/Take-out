# coding: utf-8
from rest_framework.views import APIView
from models.customer import Customer, DeliveryInformation
from models.order import Order, OrderFood
from models.complaint import Complaint
from bussiness.models.store import Store
from bussiness.models.food import Food
from lib.models.review import FoodReview, OrderReview
from lib.utils.response import JsonResponse, JsonErrorResponse
from lib.utils.misc import get_update_dict_by_list
from lib.utils.token_tools import get_token


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
            return JsonErrorResponse("Fail:" + e.message)
        print "新注册顾客id：", new_customer.id
        # 登陆
        token = get_token(username, password, "customer")
        return JsonResponse({
            "id": new_customer.id,
            "token": token
        })


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
            return JsonErrorResponse("Fail:" + e.message)
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
            return JsonErrorResponse("Fail:" + e.message)
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
            status = request.json.get("status")
            assert status in map(lambda i:i[0], Complaint.STATUS_LIST), "not valid"
            update_dict = get_update_dict_by_list(update_item, request.json)
            modify_num = Complaint.objects.filter(id=complaint_id).update(**update_dict)
            assert modify_num == 1
            return JsonResponse({})
        except Exception, e:
            return JsonErrorResponse("Update failed:" + e.message, 400)


# 订单
class OrderList(APIView):
    def get(self, request):
        # 获取订单列表
        owner = request.u
        account_type = request.account_type
        if not owner:
            return JsonErrorResponse("can't find user", 404)
        if account_type != "customer" and account_type != "bussiness":
            return JsonErrorResponse("wrong account type", 403)
        orders = [order.to_string() for order in owner.orders.all()]
        return JsonResponse({"order_list": orders})

    def post(self, request):
        # 添加订单
        try:
            customer = request.u
            note = request.json.get("note")
            delivery_information_id = request.json.get("delivery_information_id")
            store_id = request.json.get("store_id")
            food_list = request.json.get("food_list")
            store = Store.objects.get(id=store_id)
            total_price = 0

            if not all([food_list, delivery_information_id, store]):
                return JsonErrorResponse("food_list, delivery_information_id, store_id are needed", 400)

            # 检查food_list
            assert isinstance(food_list, list) and len(food_list) > 0, "food_list format wrong"
            # 检查库存+计算价格
            for order_food in food_list:
                food = store.foods.get(id=order_food['food_id'])
                food_count = int(order_food['count'])
                total_price += food.price * food_count
                assert food.stock > food_count, "food stock is not enough"
            # 检查收货信息
            delivery_information = customer.delivery_informations.get(id=delivery_information_id)
            # 检查账户类型
            assert request.account_type == "customer", "only customer can make order"

            # 创建order
            new_order = Order(
                note=note,
                total_price=total_price,
                customer=customer,
                store=store,
                delivery_information=delivery_information
            )
            new_order.save()

            # 减少库存，创建order_food
            for order_food in food_list:
                food = store.foods.get(id=order_food['food_id'])
                food_count = int(order_food['count'])
                new_stock = food.stock - food_count
                store.foods.filter(id=order_food['food_id']).update(stock=new_stock)
                OrderFood(
                    count=food_count,
                    food=food,
                    order=new_order
                ).save()

        except Exception, e:
            print e
            return JsonErrorResponse("Fail:" + e.message)
        print "新订单id：", new_order.id
        return JsonResponse({"id": new_order.id})


class OrderDetail(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonErrorResponse("Order does not exist", 404)
        return JsonResponse({"order": order.to_detail_string()})

    def put(self, request, order_id):
        # 更新订单
        try:
            action = request.json.get("action")
            order = Order.objects.get(id=order_id)
            status = order.status
            if request.account_type == "customer":
                action_to_func = {"finish": order.finish}
            else:
                action_to_func = {
                    "accept": order.accept,
                    "transport": order.transport,
                    "close": order.close,
                }
            if action not in action_to_func:
                return JsonErrorResponse("fail to action on order", 400)
            action_to_func[action]()
            # 评论商品和订单 只允许一次
            if action == "finish" and status == "3":
                order_foods = order.order_foods.all()
                order_foods_food = [i.food for i in order_foods]
                food_review_list = request.json.get("food_review_list", [])

                # 商品评论
                data = {}
                data['customer'] = request.u
                data['order'] = order
                for food_review in food_review_list:
                    try:
                        food = Food.objects.get(id = food_review.get("food_id"))
                        assert food in order_foods_food
                        data['food'] = food
                        data['content'] = food_review.get("content", "")
                        data['star'] = food_review.get("star", "5")
                        new_food_review = FoodReview(**data)
                        new_food_review.save()
                    except Exception, e:
                        print e.message
                # 订单评论
                order_review = request.json.get("order_review")
                data['store'] = order.store
                if order_review:
                    if data.get('food'):
                        data.pop('food')
                    data['delivery_time'] = order_review.get("delivery_time", 120)
                    data['content'] = order_review.get("content", "")
                    data['star'] = order_review.get("star", "5")
                    new_order_review = OrderReview(**data)
                    new_order_review.save()

                order_review = request.json.get("order_review")
            return JsonResponse({})
        except Exception, e:
            return JsonErrorResponse("Update failed:" + e.message, 400)
