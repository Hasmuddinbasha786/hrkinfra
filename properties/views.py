from rest_framework.viewsets import ModelViewSet
from .models import Property, Inquiry
from .serializers import PropertySerializer, InquirySerializer
from django.contrib.auth.models import User

User.objects.create_superuser("hashu", "youremail@gmail.com", "12345678")

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_serializer_context(self):
        return {"request": self.request}


class InquiryViewSet(ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer