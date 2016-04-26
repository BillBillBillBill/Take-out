# coding: utf-8
from bussiness.models.seller import Seller
from conn import redisClient
import json


USER_MODEL_MAP = {
    "admin": Seller,
    "customer": Seller,
    "bussiness": Seller,
}


class TokenMiddleware(object):
    def process_request(self, request):
        print request.json
        request.u = None
        request.account_type = None
        token = request.json.get('token')
        print "token:", token
        if not token:
            return
        # check token
        if token and len(token.split('$')) == 5:
            info = token.split('$')
            account_type = info[1]
            user_id = info[2]
            if redisClient.get("token:%s:%s" % (account_type, user_id)) == token:
                if account_type not in USER_MODEL_MAP:
                    return
                user = USER_MODEL_MAP[account_type].query.get(user_id)
                request.u = user
                request.account_type = account_type


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
