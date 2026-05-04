from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from .models import *

from .serializers import PropertySerializer
from .serializers import InquirySerializer




class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer