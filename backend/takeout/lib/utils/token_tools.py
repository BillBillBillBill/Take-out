# coding: utf-8
import time
from bussiness.models.seller import Seller
from customer.models.customer import Customer
from password_tools import check_password
from takeout.conn import redisClient


USER_MODEL_MAP = {
    "admin": Seller,
    "customer": Customer,
    "bussiness": Seller,
}


def get_token(username, password, account_type):
    '''
    token格式为时间戳+账户类型(admin:管理员bussiness:用户customer:卖家)+uid+加密后的密码
    失败返回值为False
    成功返回值为token
    '''
    if account_type not in USER_MODEL_MAP:
        return False
    user = USER_MODEL_MAP[account_type].objects.get(username=username)
    if not user or not check_password(password, user.password):
        return False
    else:
        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        user_id = user.id
        token = "%s$%s$%s$%s" % (now_time, account_type, user_id, user.password)
        print "token:", token
        # 把该token存进redis中 键为id，值为token
        redisClient.set("token:%s:%s" % (account_type, user_id), token)
        return token
    return False
