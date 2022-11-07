from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from .models import USER, SERVER
from .serializer import USERSerializers, SERVERSerializers, SERVERCreateSerializers, SERVERListSerializers


@api_view(['POST'])
def USERCreate(request):
    if request.method == "POST":
        serializer = USERSerializers(data=request.data)
        if serializer.is_valid():
            try:
                data = serializer.validated_data.get("NAME")
                ob = USER.objects.get(NAME=data)
                return Response({
                    "message": "중복된 ID"
                })
            except Exception:
                serializer.save()
                return Response({
                    "message": "회원가입 완료"
                })
        return Response({
            "message": "오류 발생"
        })


@api_view(['POST'])
def Login(request):
    if request.method == "POST":
        serializer = USERSerializers(data=request.data)
        if serializer.is_valid():
            try:
                data = serializer.validated_data.get("NAME")
                ob = USER.objects.get(NAME=data)
                data2 = serializer.validated_data.get("PASSWORD")
                if ob.PASSWORD == data2:
                    return Response({
                        "id": ob.id,
                        "name": data
                    })
                return Response({
                    "message": "잘못된 password"
                })
            except Exception:
                return Response({
                    "message": "잘못된 id"
                })
        return Response({
            "message": "오류 발생"
        })


# 상태 표시 코드 추과
@api_view(['GET'])
def SERVER_list(request, pk):
    if request.method == "GET":
        user = USER.objects.get(pk=pk)
        data = SERVER.objects.filter(USER=user).order_by('-id')
        for i in data:
            try:
                response = requests.get(i.LINK)
                if response.status_code == 200:
                    i.STATUS = 1
                elif response.status_code == 400:
                    i.STATUS = 2
            except Exception:
                i.STATUS = 3
        serializer = SERVERListSerializers(data, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def SERVER_C(request):
    if request.method == "POST":
        serializer = SERVERCreateSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data.get("USER")
            ob = USER.objects.get(pk=data)
            serializer.save(USER=ob)
            return Response({
                "message": "저장 완료"
            })
        return Response({
            "message": "오류 발생"
        })


@api_view(['GET', 'PUT', 'DELETE'])
def SERVER_detail(request, pk):
    data = SERVER.objects.get(pk=pk)
    if request.method == "GET":
        serializer = SERVERSerializers(data)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = SERVERSerializers(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "수정 완료"
            })
        return Response({
            "message": "오류 발생"
        })
    if request.method == "DELETE":
        data.delete()
        return Response({
            "message": "삭제 완료"
        })
