# coding: utf-8
import redis
from settings import DATABASES

redisClient = redis.Redis(host=DATABASES['redis']['HOST'], port=DATABASES['redis']['PORT'])
