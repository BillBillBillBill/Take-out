# coding: utf-8
from hashlib import sha256
from hmac import HMAC
import random


def check_password(password, enc_password):
    '''
    检验密码是否正确，输入为原始密码与加密后的密码
    返回值为True或False
    '''
    try:
        salt = enc_password.split('$')[0]
        new_enc_password = get_enc_password(password, salt)
        return enc_password == new_enc_password
    except Exception:
        return False


def get_enc_password(raw_password, salt=None):
    '''
    密码加密，输入为盐
    若没有输入盐，随机生成盐
    返回值为salt$password
    '''
    if salt is None:
        salt = sha256(str(random.random())).hexdigest()[-8:]
    if isinstance(raw_password, unicode):
        raw_password = raw_password.encode('utf-8')
    enc_password = '%s$%s' % (salt, HMAC(str(salt), str(raw_password), sha256).hexdigest())
    return enc_password


def check_password(password, enc_password):
    '''
    检验密码是否正确，输入为原始密码与加密后的密码
    返回值为True或False
    '''
    try:
        salt = enc_password.split('$')[0]
        new_enc_password = get_enc_password(password, salt)
        return enc_password == new_enc_password
    except Exception:
        return False
