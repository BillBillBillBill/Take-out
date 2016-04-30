# coding: utf-8
from rest_framework.views import APIView
from models.admin import Admin
from lib.utils.response import JsonResponse, JsonErrorResponse
from lib.utils.misc import get_update_dict_by_list


class AdminList(APIView):
    def get(self, request):
        # 获取管理员列表
        admins = [admin.to_string() for admin in Admin.objects.all()]
        return JsonResponse({"admin_list": admins})

    def post(self, request):
        # 注册
        username = request.json.get("username")
        password = request.json.get("password")
        nickname = request.json.get("nickname")
        account_type = request.json.get("account_type")
        if not all([username, password, nickname, account_type]):
            return JsonErrorResponse("username, password, nickname, account_type are needed", 400)
        new_admin = Admin(
            username=username,
            password=password,
            nickname=nickname,
            account_type=account_type
        )
        try:
            new_admin.save()
        except Exception, e:
            print e
            return JsonErrorResponse("Fail" + e.message)
        print "新注册管理员id：", new_admin.id
        return JsonResponse({"id": new_admin.id})


class AdminDetail(APIView):
    def get(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
        except Admin.DoesNotExist:
            return JsonErrorResponse("Admin does not exist", 404)
        return JsonResponse({"admin": admin.to_detail_string()})

    def put(self, request, admin_id):
        # 更新个人信息
        update_item = ['nickname', 'password']
        update_dict = get_update_dict_by_list(update_item, request.json)
        modify_num = Admin.objects.filter(id=admin_id).update(**update_dict)
        if modify_num == 1:
            return JsonResponse({})
        return JsonErrorResponse("Update failed", 400)
