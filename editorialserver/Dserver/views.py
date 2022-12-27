from rest_framework import status
from rest_framework.response import Response
from django.db.models import Avg
from datetime import timedelta
from rest_framework.decorators import api_view
from django.utils import timezone

from .models import CAMERA, TEMPERATURE, HUMIDITY, REMNANT_W
from .serializer import REMNANT_WSerializer, CAMERASerializer, TEMPERATURESerializer, HUMIDITYSerializer


@api_view(['GET'])
def status1(request):
    if request.method == "GET":
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def last_TEMPERATURE(request):
    if request.method == "GET":
        data = TEMPERATURE.objects.last()
        serializer = TEMPERATURESerializer(data)
        return Response(serializer.data)


@api_view(['GET'])
def last_HUMIDITY(request):
    if request.method == "GET":
        data = HUMIDITY.objects.last()
        serializer = HUMIDITYSerializer(data)
        return Response(serializer.data)


@api_view(['GET'])
def last_REMNANT_W(request):
    if request.method == "GET":
        data = REMNANT_W.objects.last()
        serializer = REMNANT_WSerializer(data)
        return Response(serializer.data)


@api_view(['GET'])
def list_TEMPERATURE(request, i):
    if request.method == "GET":
        data = TEMPERATURE.objects.all().order_by('-id')[i * 7:i * 7 + 7]
        serializer = TEMPERATURESerializer(data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def list_HUMIDITY(request, i):
    if request.method == "GET":
        data = HUMIDITY.objects.all().order_by('-id')[i * 7:i * 7 + 7]
        serializer = HUMIDITYSerializer(data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def M_list_TEMPERATURE(request, i):
    if request.method == "GET":
        data = TEMPERATURE.objects.all().order_by('-id')[i * 4:i * 4 + 4]
        serializer = TEMPERATURESerializer(data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def M_list_HUMIDITY(request, i):
    if request.method == "GET":
        data = HUMIDITY.objects.all().order_by('-id')[i * 4:i * 4 + 4]
        serializer = HUMIDITYSerializer(data, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def AVG_TEMPERATURE(request):
    if request.method == "GET":
        data = TEMPERATURE.objects.last()
        data1 = TEMPERATURE.objects.filter(TIME__range=[timezone.now() - timedelta(days=1), timezone.now()]).aggregate(
            Avg('TEMP'))
        d1 = data1['TEMP__avg']
        data2 = TEMPERATURE.objects.filter(TIME__range=[timezone.now() - timedelta(days=7), timezone.now()]).aggregate(
            Avg('TEMP'))
        d2 = data2['TEMP__avg']
        return Response({
            "now": data.TEMP,
            "day": d1,
            "week": d2
        })


@api_view(['GET'])
def AVG_HUMIDITY(request):
    if request.method == "GET":
        data = HUMIDITY.objects.last()
        data1 = HUMIDITY.objects.filter(TIME__range=[timezone.now() - timedelta(days=1), timezone.now()]).aggregate(
            Avg('DEGREE'))
        d1 = data1['DEGREE__avg']
        data2 = HUMIDITY.objects.filter(TIME__range=[timezone.now() - timedelta(days=7), timezone.now()]).aggregate(
            Avg('DEGREE'))
        d2 = data2['DEGREE__avg']
        return Response({
            "now": data.DEGREE,
            "day": d1,
            "week": d2
        })


@api_view(['GET', 'DELETE', 'PUT'])
def CAMERA_link(request, pk):
    try:
        ob = CAMERA.objects.get(pk=pk)
        if request.method == "GET":
            serializer = CAMERASerializer(ob)
            return Response(serializer.data)
        if request.method == "PUT":
            serializer = CAMERASerializer(ob, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "수정 완료 "
                })
            return Response({
                "message": "오류 발생."
            })
        if request.method == "DELETE":
            ob.delete()
            return Response({
                "message": "삭제 완료"
            })
    except Exception:
        return Response({
            "message": "객체 없음."
        })


@api_view(['POST', 'GET'])
def CAMARA_LINK_C(request):
    if request.method == "POST":
        serializer = CAMERASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "등록 완료"
            })
        return Response({
            "message": "오류 발생"
        })
    if request.method == "GET":
        data = CAMERA.objects.all()
        serializer = CAMERASerializer(data, many=True)
        return Response(serializer.data)
