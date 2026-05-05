from rest_framework.viewsets import ModelViewSet
from .models import Property, Inquiry
from .serializers import PropertySerializer, InquirySerializer
from django.contrib.auth.models import User

def create_admin():
    try:
        if not User.objects.filter(username="hashu").exists():
            User.objects.create_superuser("hashu", "youremail@gmail.com", "12345678")
            print("Superuser created")
    except Exception as e:
        print("Error creating superuser:", e)

create_admin()

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_serializer_context(self):
        return {"request": self.request}


class InquiryViewSet(ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer