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
from django.http import JsonResponse

def citypage(request,ipaddr):
    try:
        r = requests.get("http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting,query".format(ipaddr)).json()

        context = {
            'ipaddr' : ipaddr,
            'city' : r['city'],
        }
    except:
        context = {
        'Error' : 'Someting wrong happen',
        }
    
    return JsonResponse(context)

def proxypage(request,ipaddr):
    try:
        r = requests.get("http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting,query".format(ipaddr)).json()

        context = {
            'ipaddr' : ipaddr,
            'proxy' : r['proxy'],
        }
    except:
        context = {
        'Error' : 'Someting wrong happen',

    

    }
    return JsonResponse(context)



def regionpage(request,ipaddr):
    try:
        r = requests.get("http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting,query".format(ipaddr)).json()

        context = {
            'ipaddr' : ipaddr,
            'region' : r['regionName'],
        }
    except:
        context = {
        'Error' : 'Someting wrong happen',

    

    }
    return JsonResponse(context)


def latpage(request,ipaddr):
    try:
        r = requests.get("http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting,query".format(ipaddr)).json()

        context = {
            'ipaddr' : ipaddr,
            'lat' : r['lat'],
        }
    except:
        context = {
        'Error' : 'Someting wrong happen',

    

    }
    return JsonResponse(context)


def lonpage(request,ipaddr):
    try:
        r = requests.get("http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting,query".format(ipaddr)).json()

        context = {
            'ipaddr' : ipaddr,
            'lon' : r['lon'],
            }
    except:
        context = {
        'Error' : 'Someting wrong happen',

    

    }
    return JsonResponse(context)



