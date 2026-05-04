from rest_framework.viewsets import ModelViewSet
from .models import Property, Inquiry
from .serializers import PropertySerializer, InquirySerializer


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class InquiryViewSet(ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer