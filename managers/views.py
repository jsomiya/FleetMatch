from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from partners.models import Registration
from partners.serializers import RegisterSerializer
import json

# Create your views here.

@api_view()
def all_service_partners(request):
    l = []
    partners = Registration.objects.all()
    for i in partners:
        serializer = RegisterSerializer(i, many= False)
        dict1 = {
            "company_name": serializer.data['company_name'],
            "services": serializer.data['services'],
            }
        print(dict1)
        # t = json.dumps(dict1)
        l.append(dict1)
        a=json.dumps(l)
    print(l)
    print(a)
    return HttpResponse(a,status = status.HTTP_200_OK)

@api_view()
def filter_partners(request):
    services = request.GET.get("company_name", None)
    print(services)
    partners = Registration.objects.filter(services = services)
    print(partners)
    for i in partners:
        serializer = RegisterSerializer(i)
        print(serializer.data)
    return HttpResponse(status = status.HTTP_200_OK)

# @api_view()
# def company()

