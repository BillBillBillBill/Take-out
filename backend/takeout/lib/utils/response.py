# coding: utf-8
from django.http import HttpResponse
import json


def JsonErrorResponse(message, status_code=400):
    try:
        data = '{"status_code": %s, "message": "%s"' % (status_code, message)
    except:
        data = '{"status_code": 400, "message": "Bad Request"}'
    return HttpResponse(
        content=data,
        content_type='text/json; charset=utf-8',
        status=status_code
    )


def JsonResponse(data, status_code=200):
    try:
        data = '{"status_code": %s, "data": %s}' % (status_code, json.dumps(data))
    except:
        data = '{"status_code": 200, "data": {}}'
    return HttpResponse(
        content=data,
        content_type='text/json; charset=utf-8',
        status=status_code
    )
