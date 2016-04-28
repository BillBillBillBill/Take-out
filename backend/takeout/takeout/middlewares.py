# coding: utf-8
from bussiness.models.seller import Seller
from conn import redisClient
import json
from lib.utils.response import JsonResponse, JsonErrorResponse


USER_MODEL_MAP = {
    "admin": Seller,
    "customer": Seller,
    "bussiness": Seller,
}


class TokenMiddleware(object):
    def process_request(self, request):
        request.u = None
        request.account_type = None
        token = request.json.get('token', None) or request.META.get("HTTP_AUTHORIZATION_TOKEN", None)
        if not token:
            return
        # check token
        try:
            assert token and len(token.split('$')) == 5
            info = token.split('$')
            account_type = info[1]
            user_id = info[2]
            assert redisClient.get("token:%s:%s" % (account_type, user_id)) == token
            assert account_type in USER_MODEL_MAP
            user = USER_MODEL_MAP[account_type].objects.get(id=user_id)
            request.u = user
            request.account_type = account_type
        except AssertionError:
            return JsonErrorResponse("Token Auth Fail", 403)


class JsonMiddlerware(object):
    def process_request(self, request):
        try:
            request.json = json.loads(request.body)
        except:
            request.json = {}


class TestMiddlerware(object):
    def process_request(self, request):
        if request.u:
            print request.u.username
        return None
