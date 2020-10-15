from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from API.models import API
from API.serializers import APISerializer

@csrf_exempt
def API_list(request):
   
    if request.method == 'GET':
        APIs = API.objects.all()
        serializer = APISerializer(APIs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = APISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def API_detail(request, pk):
    """
    Retrieve, update or delete a code API.
    """
    try:
        API = API.objects.get(pk=pk)
    except API.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = APISerializer(API)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = APISerializer(API, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        API.delete()
        return HttpResponse(status=204)