from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db.models import Q, Avg
from datetime import date, datetime, timedelta
from rest_framework.decorators import api_view
from django.utils import timezone