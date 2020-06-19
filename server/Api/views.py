'''
  developed by Ashkan Ganj
  Github:https://github.com/Ashkan-agc
'''

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from TimeTracker.models import Sites, UserProfile
from insctructions.dataFunc import DataInstruct
from insctructions.aggregator import Aggregators

import time
import math
import json
import datetime

dataInsctance = DataInstruct()


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentications"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


@api_view(['POST', ])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def UpdateAvtive(request):
    req = json.loads(request.body.decode('utf-8'))
    if req:
        try:
            url = req["url"]
            time = req["time"]
            mainUrl = dataInsctance.url_strip(url)
            userId = request.user.id
            if mainUrl != '' and mainUrl not in ['chrome:', 'edge:']:
                dataInsctance.CalculateTimeInstructions(mainUrl, userId, time)
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        except Exception as identifier:
            return HttpResponse(status=400)

    else:
        return HttpResponse(status=400)


@login_required(login_url='login')
def get_data(request):
    weekDay = {}
    label = []
    data = []
    minute = []
    percentage = []

    q = Sites.objects
    sites = q.filter(user_id=request.user.id).order_by('time').all()

    for site in sites:
        label.append(site.url)
        sec = site.time
        data.append(sec)
        minute.append(dataInsctance.get_minute(sec))

    for item in data:
        percentage.append(dataInsctance.get_percentage(item, data))
    data = {
        "daily": dataInsctance.get_week_days_data(request.user.id),
        "label": label,
        "data": data,
        "min": minute,
        "percentage": percentage
    }
    return JsonResponse(data)
