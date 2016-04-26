# coding: utf-8
from lib.utils.response import JsonResponse, JsonErrorResponse
from rest_framework import status
from lib.utils.token_tools import get_token
import json


def login(request, account_type):
    try:
        if request.method == 'POST':
            data = request.json
            username = data.get('username')
            password = data.get('password')
            token = get_token(username, password, account_type)
            if token:
                return JsonResponse({"token": token}, status.HTTP_200_OK)
    except:
        pass
    return JsonErrorResponse("AUTH FAIL", status.HTTP_401_UNAUTHORIZED)
