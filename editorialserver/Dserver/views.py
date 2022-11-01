from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db.models import Q, Avg
from datetime import date, datetime, timedelta
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


@api_view(['GET'])
def CAMERA_link(request,pk):
    if request.method == "GET":
        data = CAMERA.objects.last()
        serializer = CAMERASerializer(data)
        return Response(serializer.data)
