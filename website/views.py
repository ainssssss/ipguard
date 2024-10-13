from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.conf import settings
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.utils.html import strip_tags
from django.conf import settings
import json
import requests
import os

def homepage(request):
    ipaddr = request.META.get("REMOTE_ADDR")
    try:
        r = requests.get("http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting,query".format(ipaddr)).json()    
        context = {
            'ipAddr' : ipaddr,
            'city' : r['city'],
            'regionName' : r['regionName'],
            'timezone' : r['timezone'],
            'isp' : r['isp'],
            'org' : r['org'],
            'lat' : r['lat'],
            'lon' : r['lon'],
            'proxy' : r['proxy'],
            'hosting' : r['hosting'],
    }
    except:
        context = {
            'ipAddr' : ipaddr,
            'city' : 'No data',
            'regionName' : 'No data',
            'timezone' : 'No data',
            'isp' : 'No data',
            'org' : 'No data',
            'lat' : 'No data',
            'lon' : 'No data',
            'proxy' : 'No data',
            'hosting' : 'No data',
    }
 

    return render(request,'website/index.html',context=context)

def apiPage(request):
    ipaddr = request.META.get("REMOTE_ADDR")
    try:
        r = requests.get("http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting,query".format(ipaddr)).json()

        context = {
            'ipAddr' : ipaddr,
            'city' : r['city'],
            'regionName' : r['regionName'],
            'timezone' : r['timezone'],
            'isp' : r['isp'],
            'org' : r['org'],
            'lat' : r['lat'],
            'lon' : r['lon'],
            'proxy' : r['proxy'],
            'hosting' : r['hosting'],
        }

    
    except:
        context = {
            'ipAddr' : ipaddr,
            'city' : 'No data',
            'regionName' : 'No data',
            'timezone' : 'No data',
            'isp' : 'No data',
            'org' : 'No data',
            'lat' : 'No data',
            'lon' : 'No data',
            'proxy' : 'No data',
            'hosting' : 'No data',
    }


    return render(request,'website/api.html',context=context)

