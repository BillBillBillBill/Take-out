# coding: utf-8
from bussiness.models.seller import Seller
from conn import redisClient


USER_MODEL_MAP = {
    "admin": Seller,
    "customer": Seller,
    "bussiness": Seller,
}


class TokenMiddleware(object):
    def process_request(self, request):
        try:
            token = request.body.get('token', None)
        except Exception:
            request.u = None
            request.account_type = None
            return None
        if token and len(token.split('$')) == 5:
            info = token.split('$')
            account_type = info[1]
            user_id = info[2]
            if redisClient.get("token:%s:%s" % (account_type, user_id)) == token:
                if account_type not in USER_MODEL_MAP:
                    return None
                user = USER_MODEL_MAP[account_type].query.get(user_id)
                request.u = user
                request.account_type = account_type
        return None


class TestMiddlerware(object):
    def process_request(self, request):
        if request.u:
            print request.u.username
        return None
