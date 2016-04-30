# coding: utf-8
from lib.utils.response import JsonResponse, JsonErrorResponse
from rest_framework import status
from django.core.files.base import ContentFile
from lib.models.image import ImageStore


def file_uploader(request):
    try:
        if not request.u:
            JsonErrorResponse("AUTH FAIL", status.HTTP_401_UNAUTHORIZED)
        data = request.FILES.get("image")
        file_content = ContentFile(data.read())
        img = ImageStore(name = data.name, img = data)
        img.save()
        return JsonResponse({"id": img.id}, status.HTTP_200_OK)
    except:
        pass
    return JsonErrorResponse("AUTH FAIL", status.HTTP_401_UNAUTHORIZED)
