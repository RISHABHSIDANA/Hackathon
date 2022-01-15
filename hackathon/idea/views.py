from urllib import response
from django.shortcuts import render,HttpResponse
from idea.models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.decorators import api_view
from idea.serializers import *
# Create your views here.
class ProfileUserList(generics.ListCreateAPIView):
    queryset= Testing_purpose.objects.all()
    serializer_class = Testing_purposeSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['user__first_name', 'user__last_name']
    
    def get_queryset(self):
        queryset = Testing_purpose.objects.all()
        return queryset