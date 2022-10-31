from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db.models import Q
from datetime import date, datetime
from rest_framework.decorators import api_view


# @api_view(['GET'])
# def steatus_return(request):
#     if request.method == "GET":
#         time = datetime.now()