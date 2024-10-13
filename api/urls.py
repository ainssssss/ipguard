from django.urls import path
from . import views

app_name = 'api'
urlpatterns=[
    path('city/<str:ipaddr>',views.citypage, name='homepage'),
    path('proxy/<str:ipaddr>',views.proxypage, name='homepage'),
    path('region/<str:ipaddr>',views.regionpage, name='homepage'),
    path('lat/<str:ipaddr>',views.latpage, name='homepage'),
    path('lon/<str:ipaddr>',views.lonpage, name='homepage'),

]
