from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from .models import *

from .serializers import PropertySerializer
from .serializers import InquirySerializer




class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
    

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer